from django.contrib import admin
from kayitlar.models import Kullanicilar


@admin.register(Kullanicilar)
class KullanicilarAdmin(admin.ModelAdmin):
    readonly_fields = ['isim'] ## Seçilen alanların güncellenmesini engeller. Sadece okunulabilir yapar.
