from django.contrib import admin

from kayitlar.models import Kullanicilar


@admin.register(Kullanicilar)
class KullanicilarAdmin(admin.ModelAdmin):
    list_display = ['isim', 'soyisim', 'islemtarih', 'islemtarih_saniye']

    def islemtarih_saniye(self, obj):
        return obj.islemtarih.strftime("%d %b %Y %H:%M:%S")

    islemtarih_saniye.admin_order_field = 'islemtarih'
    islemtarih_saniye.short_description = 'İşlem Zamanı'
