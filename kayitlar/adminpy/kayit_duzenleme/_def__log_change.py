import inspect
from datetime import datetime

from django.contrib import admin

from kayitlar.models import Kullanicilar


@admin.register(Kullanicilar)
class KullanicilarAdmin(admin.ModelAdmin):
    list_display = ['yazar', 'isim', 'soyisim', 'aylar', 'sehir', 'islemtarih', 'decimalfield']

    # def log_change(self, request, object, message):
    #     print('------------>  Zaman: {}  .--> Def: {} <------------'.format(datetime.now(), inspect.stack()[0][3]))
    #     print('Çağıran: {}:{}, Fonksiyon:'.format(inspect.stack()[1][1], inspect.stack()[1][2]), inspect.stack()[1][3])
    #
    #     from django.contrib.admin.models import LogEntry, ADDITION
    #     from django.contrib.admin.options import get_content_type_for_model
    #
    #     ekmesaj = ' - Güncellendi'
    #     if isinstance(message, list):
    #         ekmesaj = []
    #
    #     return LogEntry.objects.log_action(
    #         user_id=request.user.pk,
    #         content_type_id=get_content_type_for_model(object).pk,
    #         object_id=object.pk,
    #         object_repr=str(object),
    #         action_flag=ADDITION,
    #         change_message=message + ekmesaj,
    #     )

    ### Kayıt güncelleme sonrası eski değeri LogEntry ye kaydetmek
    def change_view(self, request, object_id, form_url='', extra_context=None):
        print('------------>  Zaman: {}  .--> Def: {} <------------'.format(datetime.now(), inspect.stack()[0][3]))
        print('Çağıran: {}:{}, Fonksiyon:'.format(inspect.stack()[1][1], inspect.stack()[1][2]), inspect.stack()[1][3])

        ## Düzenleme öncesi var olan kayıt bilgilerine ulaşmak
        kayit_bul = self.model.objects.get(id=object_id)
        eski_deger = kayit_bul.isim

        degisiklik = super().change_view(request, object_id, form_url, extra_context)

        kayit_bul = self.model.objects.get(id=object_id)
        yeni_kayit = kayit_bul.isim

        if eski_deger != yeni_kayit:
            self.log_change(request, kayit_bul, 'Eski İsim: {}'.format(eski_deger))

        return degisiklik
