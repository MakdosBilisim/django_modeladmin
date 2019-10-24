from django.contrib import admin

from kayitlar.models import Kullanicilar


@admin.register(Kullanicilar)
class KullanicilarAdmin(admin.ModelAdmin):
    ## Kayıt ekranında tablodaki alanları (charfield, foreingkey vs..) istenilen düzende gösterir.
    ## Örn: isim ve soyisim alanı yan yana gösterilirsin.
    fields = (('isim', 'soyisim'), 'sehir', ('coklusec', 'aylar'))
