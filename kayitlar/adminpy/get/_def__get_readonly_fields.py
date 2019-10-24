from django.contrib import admin

from kayitlar.models import Kullanicilar


@admin.register(Kullanicilar)
class KullanicilarAdmin(admin.ModelAdmin):
    list_display = ['isim', 'soyisim', 'aylar']
    readonly_fields = ('isim',)

    def get_readonly_fields(self, request, obj=None):
        if obj:  ## Kayıt edildi ve düzenleniyor ise bazı alanları düzenlenemez yap
            return self.readonly_fields + ('soyisim',)
        return self.readonly_fields
