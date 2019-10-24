from django.contrib import admin
from kayitlar.models import Kullanicilar, Aylar, CokluManytoMany


@admin.register(Kullanicilar)
class KullanicilarAdmin(admin.ModelAdmin):
    list_display = ['isim', 'soyisim', 'islemtarih']
    # filter_horizontal = ('coklusec',) ## ManyToMany alanını yan yana gösterir. Soldan Sağa taşınarak seçim yapılır
    filter_vertical = ('coklusec',) ## ManyToMany alanını alt alta gösterir. Yukarıdaki alanları aşağıya taşınarak seçim yapılır


@admin.register(CokluManytoMany)
class CokluManytoManyAdmin(admin.ModelAdmin):
    list_display = ['secimler']
