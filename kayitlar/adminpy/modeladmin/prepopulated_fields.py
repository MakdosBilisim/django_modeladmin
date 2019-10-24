from django.contrib import admin
from kayitlar.models import Kullanicilar


@admin.register(Kullanicilar)
class KullanicilarAdmin(admin.ModelAdmin):

    # soyisim alanını isim ve sehir yazıldıkça (seçildikçe) otomatik tamamlar. Araya - ekler. Genelde otomatik linkler (slug) için kullanılır.
    prepopulated_fields = {"soyisim": ('isim','sehir')}

