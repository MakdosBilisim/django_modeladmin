import inspect
from datetime import datetime

from django.contrib import admin

from kayitlar.models import Kullanicilar, CokluManytoMany


@admin.register(Kullanicilar)
class KullanicilarAdmin(admin.ModelAdmin):
    list_display = ['isim', 'soyisim', 'aylar']

    def formfield_for_manytomany(self, db_field, request, **kwargs):
        print('------------>  Zaman: {}  .--> Def: {} <------------'.format(datetime.now(), inspect.stack()[0][3]))
        print('Çağıran: {}:{}, Fonksiyon:'.format(inspect.stack()[1][1], inspect.stack()[1][2]), inspect.stack()[1][3])

        gecerli_url = request.META['PATH_INFO']

        ## İlk kayıt sayfası ise
        if gecerli_url.endswith('/add/'):
            print('kayıt eklenirken')
        else:
            print('Kayıt düzenlenirken')

        if db_field.name == 'coklusec':
            ## Filtre sonuçlarını otomatik seç
            kwargs['initial'] = CokluManytoMany.objects.filter(secimler__gt=2)

            ## Sadece filtre sonucunu göster
            kwargs['queryset'] = CokluManytoMany.objects.exclude(secimler__endswith='as')

        form_alanlari = super().formfield_for_manytomany(db_field, request, **kwargs)

        if db_field.name == 'coklusec':
            ## ManytoMany içeriklerine ek bilgiler ekle
            form_alanlari.label_from_instance = lambda instance: '{} (ID: {}) : {}'.format(instance.__str__(), instance.id, instance.secimler.upper())

        return form_alanlari
