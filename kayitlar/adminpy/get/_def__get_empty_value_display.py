import inspect
from datetime import datetime

from django.contrib import admin

from kayitlar.models import Kullanicilar


@admin.register(Kullanicilar)
class KullanicilarAdmin(admin.ModelAdmin):
    list_display = ['isim', 'soyisim', 'aylar', 'sehir', 'decimalfield']

    ## Özel alanlar hariç tüm boş geçilebilen alanlar için boş kayıt değeri
    empty_value_display = '-Seçilmedi-'

    def get_empty_value_display(self):
        print('~~~~~> admin.py  Zaman: {}  .--> Def: {} <------------'.format(datetime.now(), inspect.stack()[0][3]))

        try:
            print("~~~~~> admin.py self.empty_value_display: {}".format(self.empty_value_display))
        except AttributeError:
            print("~~~~~> admin.py self.admin_site.empty_value_display: {}".format(self.admin_site.empty_value_display))


# Özel alanlar ve ModelAdmin hariç tüm modeller için boş geçilebilen alanlar için boş kayıt değeri
admin.site.empty_value_display = '(Seçilmedi)'