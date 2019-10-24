import inspect
from datetime import datetime

from django.contrib import admin

from kayitlar.models import Kullanicilar


@admin.register(Kullanicilar)
class KullanicilarAdmin(admin.ModelAdmin):
    list_display = ['yazar', 'isim', 'soyisim', 'aylar', 'sehir', 'islemtarih', 'decimalfield']

    def log_deletion(self, request, object, object_repr):
        from django.contrib.admin.options import get_content_type_for_model
        from django.contrib.admin.models import LogEntry, DELETION

        return LogEntry.objects.log_action(
            user_id=request.user.pk,
            content_type_id=get_content_type_for_model(object).pk,
            object_id=object.pk,
            object_repr=object_repr,
            action_flag=DELETION,
            change_message=object_repr
        )

    def delete_view(self, request, object_id, extra_context=None):
        print('------------>  Zaman: {}  .--> Def: {} <------------'.format(datetime.now(), inspect.stack()[0][3]))
        print('Çağıran: {}:{}, Fonksiyon:'.format(inspect.stack()[1][1], inspect.stack()[1][2]), inspect.stack()[1][3])

        ## Kayıt silmeden öncesi var olan kayıt bilgilerine ulaşmak
        kayit_bul = self.model.objects.get(id=object_id)

        silme_islemi = super().delete_view(request, object_id, extra_context)

        ### Kayıt silinmeden LogEntry ye ek bilgi girmek
        self.log_deletion(request, kayit_bul, 'Kullanıcı Tarayıcısı: {}'.format(request.META['HTTP_USER_AGENT']))

        return silme_islemi
