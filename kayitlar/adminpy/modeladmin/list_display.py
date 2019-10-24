from django.contrib import admin

from kayitlar.models import Kullanicilar

@admin.register(Kullanicilar)
class KullanicilarAdmin(admin.ModelAdmin):
    list_display = ['isim', 'soyisim', 'islemtarih', 'islemtarih_saniye', 'id']
    # list_display = [field.attname for field in Kullanicilar._meta.fields]
    # list_display = [field.attname for field in Kullanicilar._meta.fields if field.attname != 'id']

