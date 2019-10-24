from django.contrib import admin

from kayitlar.models import Kullanicilar


@admin.register(Kullanicilar)
class KullanicilarAdmin(admin.ModelAdmin):
    list_display = ['isim', 'soyisim', 'aylar']
    search_fields = ['isim', 'soyisim', 'aylar__ay_ismi']
    # search_fields = ['isim', 'soyisim']
