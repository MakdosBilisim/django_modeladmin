import inspect
from datetime import datetime

from django.contrib import admin

from kayitlar.models import Kullanicilar


class KullanicilarAdmin(admin.ModelAdmin):

    def __init__(self, model, admin_site):
        ### __init__ bir kere çağrılır ve diğer alanları ezer
        print("__init__ çağrıldı")
        print('Zaman: {}  .--> Def: {}'.format(datetime.now(), inspect.stack()[0][3]))
        # self.list_display = [field.attname for field in Kullanicilar._meta.fields if field.attname != 'id']
        super().__init__(model, admin_site)


admin.site.register(Kullanicilar, KullanicilarAdmin)
