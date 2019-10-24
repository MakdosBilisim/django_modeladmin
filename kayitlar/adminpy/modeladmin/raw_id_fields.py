from django.contrib import admin
from kayitlar.models import Kullanicilar


@admin.register(Kullanicilar)
class KullanicilarAdmin(admin.ModelAdmin):
    raw_id_fields = ['aylar', 'coklusec'] ## Foreingkey ve Manytomany alanlarını ek pencerede açar ama sadece idlerini gösterir
