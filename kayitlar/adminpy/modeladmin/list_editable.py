from django.contrib import admin

from kayitlar.models import Kullanicilar


class KullanicilarAdmin(admin.ModelAdmin):

    list_display = ['isim','']
    list_editable = ['isim']#list_editable olması için list display de bulunması gerekir fakat list_display_links te olanlar KULLANILAMAZ.

admin.site.register(Kullanicilar, KullanicilarAdmin)
