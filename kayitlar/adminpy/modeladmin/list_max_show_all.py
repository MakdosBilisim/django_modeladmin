from django.contrib import admin

from kayitlar.models import Kullanicilar


class KullanicilarAdmin(admin.ModelAdmin):

    list_per_page = 10  ## Sayfada gösterilecek kayıt sayısı
    list_max_show_all = 10  ## Tümünü seç te gösterilecek en fazla kayıt sayısı

admin.site.register(Kullanicilar, KullanicilarAdmin)
