from django.contrib import admin
from kayitlar.models import Kullanicilar


@admin.register(Kullanicilar)
class KullanicilarAdmin(admin.ModelAdmin):
    radio_fields = {"aylar": admin.VERTICAL} ## Seçilen Foreignkey alanını selectbox yerine radio-button yapar ve alt alta dizer
    # radio_fields = {"aylar": admin.HORIZONTAL} ## Seçilen Foreignkey alanını selectbox yerine radio-button yapar ve yan yana dizer