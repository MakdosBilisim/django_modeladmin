import inspect
from datetime import datetime

from django.contrib import admin

from kayitlar.models import Kullanicilar


@admin.register(Kullanicilar)
class KullanicilarAdmin(admin.ModelAdmin):
    list_display = ['isim', 'soyisim', 'aylar']

    ### Modeldeki bir alana göre objeye ulaşmak. form_field gönderilmez ise ID (pk) ye göre arar
    def get_object(self, request, object_id, from_field=None, kayit_coklu=False):
        queryset = self.get_queryset(request)
        print(queryset)
        model = queryset.model
        print(model)
        field = model._meta.pk if from_field is None else model._meta.get_field(from_field)
        print(field)

        if kayit_coklu:
            ### Sorguya uygun olan tüm kayıtları göstermek
            return queryset.filter(**{field.name: object_id})
        else:
            ## Sorguya uyan ilk kaydı göstermek
            try:
                object_id = field.to_python(object_id)
                return queryset.get(**{field.name: object_id})
            except (model.DoesNotExist, ValueError):
                return None

    def get_list_display(self, request):
        print('------------>  Zaman: {}  .--> Def: {} <------------'.format(datetime.now(), inspect.stack()[0][3]))
        print('Çağıran: {}:{}, Fonksiyon:'.format(inspect.stack()[1][1], inspect.stack()[1][2]), inspect.stack()[1][3])

        kayit_coklu = True
        ### isim alanı rewq olan ve eşleşen İLK kaydı (ya da kayıtları) bul
        obj = self.get_object(request, 'reqw', from_field='isim', kayit_coklu=kayit_coklu)

        if kayit_coklu:
            print(obj.count())

        print(obj)

        return self.list_display
