from django.contrib import admin

from kayitlar.models import Kullanicilar


class KullanicilarAdmin(admin.ModelAdmin):
    list_display = ['isim', 'soyisim', 'islemtarih', 'islemtarih_saniye', 'id']
    # list_display = [field.attname for field in Kullanicilar._meta.fields]
    # list_display = [field.attname for field in Kullanicilar._meta.fields if field.attname != 'id']

    # list_display_links = list_display
    list_display_links = ['soyisim', 'id']
    # list_display_links = [field.attname for field in Kullanicilar._meta.fields]
    # list_display_links = [field.attname for field in Kullanicilar._meta.fields if field.attname != 'id'] # list_display de olmayan alanlar eklenemez. # Foreignkey ile kullanılamaz.


admin.site.register(Kullanicilar, KullanicilarAdmin)
