import inspect
from datetime import datetime

from django.contrib import admin

from kayitlar.models import Kullanicilar


@admin.register(Kullanicilar)
class KullanicilarAdmin(admin.ModelAdmin):
    list_display = ['isim', 'soyisim', 'aylar']

    class Media:
        pass

    fieldsets = [
        ('Önce Gösterilecekler', {'classes': ('wide', 'collapse'), 'fields': ('sehir', 'decimalfield',)}),
        ('Sonraki Sayfa Üst', {'classes': ('wide',), 'fields': ('coklusec', 'aylar',)}),
        ('Sonraki Sayfa Alt', {'classes': ('wide', 'collapse'), 'fields': ('isim', 'soyisim',)}),
    ]

    add_fieldsets = [
        ('Önce Gösterilecekler', {'fields': ('sehir', 'decimalfield',)}),
    ]

    ## İlk kayıt ve kayıt düzenleme sırasında özel işlemler
    def get_fieldsets(self, request, obj=None):

        print('------------>  Zaman: {}  .--> Def: {} <------------'.format(datetime.now(), inspect.stack()[0][3]))
        print('Çağıran: {}:{}, Fonksiyon:'.format(inspect.stack()[1][1], inspect.stack()[1][2]), inspect.stack()[1][3])

        gecerli_url = request.META['PATH_INFO']

        ## İlk kayıt sayfası ise
        if gecerli_url.endswith('/add/'):
            self.save_on_top = False
            self.Media.css = {'all': ('admin/css/add__ozel__style.css',)}
            self.readonly_fields = ['isim']
        else:
            ## Kayıt düzenleme sayfası ise
            self.save_on_top = True
            self.Media.css = {'all': ('admin/css/change__ozel__style.css',)}
            self.readonly_fields = ['soyisim']

        if not obj:
            return self.add_fieldsets
        else:
            return self.fieldsets
