from django.contrib import admin
from kayitlar.models import Kullanicilar, Aylar


@admin.register(Kullanicilar)
class KullanicilarAdmin(admin.ModelAdmin):
    ## Foreingkey için otomatik tamamlama yapılabilir. Foreingkey e bağlı tablo (Aylar) ModelAdmin de search_fields kullanılmalı.
    autocomplete_fields = ['aylar']


@admin.register(Aylar)
class AylarAdmin(admin.ModelAdmin):
    ## Foreingkey ile bağlı tablolardan arama yapılabilinmesi için search_fields aktif edilmeli.
    search_fields = ['ay_ismi']
