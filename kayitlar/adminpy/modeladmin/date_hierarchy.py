from django.contrib import admin

from kayitlar.models import Kullanicilar


@admin.register(Kullanicilar)
class KullanicilarAdmin(admin.ModelAdmin):
    date_hierarchy = 'islemtarih'  # Tek seçim olduğu için string veya tuple olmalı
