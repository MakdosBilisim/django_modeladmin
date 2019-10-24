import inspect
from datetime import datetime

from django.contrib import admin

from kayitlar.models import Kullanicilar


@admin.register(Kullanicilar)
class KullanicilarAdmin(admin.ModelAdmin):
    list_display = ['isim', 'soyisim', 'aylar']

    ## Queryset delete fonksiyonu
    def delete_queryset(self, request, queryset):
        print('------------>  Zaman: {}  .--> Def: {} <------------'.format(datetime.now(), inspect.stack()[0][3]))
        print('Çağıran: {}:{}, Fonksiyon:'.format(inspect.stack()[1][1], inspect.stack()[1][2]), inspect.stack()[1][3])

        queryset.delete()
