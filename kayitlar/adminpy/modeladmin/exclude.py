from django.contrib import admin

from kayitlar.models import Kullanicilar


@admin.register(Kullanicilar)
class KullanicilarAdmin(admin.ModelAdmin):
    ## Kayıt girilirken zorunlu alan olsa dahi form da göstermez.
    exclude = ['isim']
