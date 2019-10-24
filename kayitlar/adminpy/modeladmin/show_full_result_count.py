from django.contrib import admin
from kayitlar.models import Kullanicilar


@admin.register(Kullanicilar)
class KullanicilarAdmin(admin.ModelAdmin):
    search_fields = ['isim']
    show_full_result_count = False  ## search_fields ile kullanılabilir. Arama sonrası seçim yapılırken değer False ise Ara butonunun yanında Tümünü Seç linki aktif olur.
