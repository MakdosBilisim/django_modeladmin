from django.contrib import admin

from kayitlar.models import Kullanicilar, Aylar, CokluManytoMany


@admin.register(Kullanicilar)
class KullanicilarAdmin(admin.ModelAdmin):
    list_display = ['yazar', 'isim', 'soyisim', 'aylar', 'sehir', 'islemtarih', 'toplantitarih', 'decimalfield']


@admin.register(Aylar)
class AylarAdmin(admin.ModelAdmin):
    list_display = ['ay_ismi']


@admin.register(CokluManytoMany)
class CokluManytoManyAdmin(admin.ModelAdmin):
    list_display = ['secimler']


from django.contrib.admin.models import LogEntry

admin.site.register(LogEntry)
