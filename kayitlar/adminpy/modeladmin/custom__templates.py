from django.contrib import admin

from kayitlar.models import Kullanicilar


@admin.register(Kullanicilar)
class KullanicilarAdmin(admin.ModelAdmin):
    list_display = ['isim', 'soyisim', 'islemtarih', 'islemtarih_saniye']

    # # Template
    ####### settings.TEMPLATES.APP_DIRS: True olmalı #########
    # add_form_template = None
    # change_form_template = None
    change_list_template = 'admin/kayitlar/kullanicilar/change_list.html' ## Sadece kayitlar uygulamasındaki Kullancilar modeline ait
    delete_confirmation_template = 'admin/kayitlar/kayit_sil.html' ## Tüm kayitlar uygulamasına ait modeller. Örn: Kullanicilar, Aylar, CokluManytoMany
    delete_selected_confirmation_template = 'admin/secili_kayitlari_sil.html'
    object_history_template = 'admin/gecmis_eylemler.html'
    # popup_response_template = None
