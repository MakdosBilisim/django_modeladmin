from django.contrib import admin

from kayitlar.models import Kullanicilar


@admin.register(Kullanicilar)
class KullanicilarAdmin(admin.ModelAdmin):
    save_on_top = True  ##Kayıt giriş veya düzenlemede kaydet butonları üstte de gösterilir
