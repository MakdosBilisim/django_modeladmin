from django.contrib import admin

from kayitlar.models import Kullanicilar


class KullanicilarAdmin(admin.ModelAdmin):
    list_display = ['isim', 'soyisim', 'islemtarih', 'islemtarih_saniye', 'id']
    # list_display = [field.attname for field in Kullanicilar._meta.fields]
    # list_display = [field.attname for field in Kullanicilar._meta.fields if field.attname != 'id']

    # ordering = list_display
    # ordering = ['-isim']
    ordering = ['isim', '-soyisim']

admin.site.register(Kullanicilar, KullanicilarAdmin)
