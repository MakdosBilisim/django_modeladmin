import inspect
from datetime import datetime

from django.contrib import admin
from django.contrib.admin.utils import construct_change_message

from kayitlar.models import Kullanicilar


@admin.register(Kullanicilar)
class KullanicilarAdmin(admin.ModelAdmin):
    list_display = ['isim', 'soyisim', 'aylar']

    ## Güncelleme yapılan alanlar ve eski değerler
    def construct_change_message(self, request, form, formsets, add=False):
        print('------------>  Zaman: {}  .--> Def: {} <------------'.format(datetime.now(), inspect.stack()[0][3]))
        print('Çağıran: {}:{}, Fonksiyon:'.format(inspect.stack()[1][1], inspect.stack()[1][2]), inspect.stack()[1][3])

        ## Değişen alanların json karşılığı
        degisen_alanlar = construct_change_message(form, formsets, add)
        print(degisen_alanlar)

        ## Form da değişen eski değerler
        degisen_degerler = {}
        for guncellenen_alan in form.changed_data:

            ## ManytoMany alanında çoklu değer döneceği için döngüye alıyoruz
            if isinstance(form.initial[guncellenen_alan], list):
                list_degisenler = []
                for k in form.initial[guncellenen_alan]:
                    list_degisenler.append(str(k))
                    degisen_degerler[guncellenen_alan] = list_degisenler

            if isinstance(form.initial[guncellenen_alan], str):
                degisen_degerler[guncellenen_alan] = str(form.initial[guncellenen_alan])

        print(degisen_degerler)

        return degisen_alanlar