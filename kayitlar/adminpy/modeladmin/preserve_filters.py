from django.contrib import admin

from kayitlar.models import Kullanicilar


@admin.register(Kullanicilar)
class KullanicilarAdmin(admin.ModelAdmin):
    preserve_filters = False  ## True iken Kayıt ekleme, düzenleme ve silme sonrası FİLTRE (arama değil) varsa aynen korur.
