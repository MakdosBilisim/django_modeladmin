from django.contrib import admin

from kayitlar.models import Kullanicilar


class KullanicilarAdmin(admin.ModelAdmin):
    list_display = ['isim', 'soyisim', 'islemtarih', 'islemtarih_saniye', 'id']

    list_select_related = ('aylar',)  ## N+1 sorunu için tek seferde birleştirerek çağır. # () tuple kullanılacak ise tek eleman olamaz.


admin.site.register(Kullanicilar, KullanicilarAdmin)
