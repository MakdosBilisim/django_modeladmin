from django.contrib import admin
from kayitlar.models import Kullanicilar


@admin.register(Kullanicilar)
class KullanicilarAdmin(admin.ModelAdmin):
    list_display = ['isim', 'soyisim', 'islemtarih']

    # list_display ile birlikte kullanılmalı. Eklenen alanlar change_listte ki grid başlıklarında sıralama yaptırmaya izin verir. Kullanılmaz ise tüm alanların başlıklarında sıralama aktiftir.
    sortable_by = ['isim', 'soyisim']

