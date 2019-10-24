import inspect
from datetime import datetime

from django.contrib import admin

from kayitlar.models import Kullanicilar


@admin.register(Kullanicilar)
class KullanicilarAdmin(admin.ModelAdmin):
    list_display = ['yazar', 'isim', 'soyisim', 'aylar', 'sehir', 'islemtarih', 'decimalfield']

    ### Kayıt girildikten sonra geçmiş loglara özel kayıtlar ekle
    def log_addition(self, request, object, message):
        print('------------>  Zaman: {}  .--> Def: {} <------------'.format(datetime.now(), inspect.stack()[0][3]))
        print('Çağıran: {}:{}, Fonksiyon:'.format(inspect.stack()[1][1], inspect.stack()[1][2]), inspect.stack()[1][3])

        from django.contrib.admin.models import LogEntry, ADDITION
        from django.contrib.admin.options import get_content_type_for_model

        ekmesaj = ' - Tüm özel kayıtlara eklenecek mesaj'
        if isinstance(message, list):
            ekmesaj = []

        return LogEntry.objects.log_action(
            user_id=request.user.pk,
            content_type_id=get_content_type_for_model(object).pk,
            object_id=object.pk,
            object_repr=str(object),
            action_flag=ADDITION,
            change_message=message + ekmesaj,
        )

    ## Kayıt ekleme sonrası işlem yaptırmak
    def response_add(self, request, obj, post_url_continue=None):
        print('------------>  Zaman: {}  .--> Def: {} <------------'.format(datetime.now(), inspect.stack()[0][3]))
        print('Çağıran: {}:{}, Fonksiyon:'.format(inspect.stack()[1][1], inspect.stack()[1][2]), inspect.stack()[1][3])

        self.log_addition(request, obj, 'Ek Bilgi: Kullanıcı Tarayıcısı: {}'.format(request.META['HTTP_USER_AGENT']))
        self.log_addition(request, obj, 'Ek Bilgi: REMOTE_ADDR: {}'.format(request.META['REMOTE_ADDR']))

        return super().response_add(request, obj, post_url_continue)
