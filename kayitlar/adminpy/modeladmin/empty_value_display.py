from django.contrib import admin

from kayitlar.models import Kullanicilar


@admin.register(Kullanicilar)
class KullanicilarAdmin(admin.ModelAdmin):
    list_display = ['isim', 'soyisim', 'aylar_emptvalue']

    ## Özel alanlar hariç tüm boş geçilebilen alanlar için boş kayıt değeri
    empty_value_display = '-Seçilmedi-'

    def aylar_emptvalue(self, obj):
        return obj.aylar
    ## Özel alan için boş alan değeri
    aylar_emptvalue.empty_value_display = 'Seçilmedi'
    aylar_emptvalue.short_description = 'İşlem Zamanı'

#Özel alanlar ve ModelAdmin hariç tüm modeller için boş geçilebilen alanlar için boş kayıt değeri
admin.site.empty_value_display = '(Seçilmedi)'