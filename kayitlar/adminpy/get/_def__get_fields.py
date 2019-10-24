import inspect
from datetime import datetime

from django.contrib import admin

from kayitlar.models import Kullanicilar


@admin.register(Kullanicilar)
class KullanicilarAdmin(admin.ModelAdmin):
    list_display = ['yazar', 'isim', 'soyisim', 'aylar', 'sehir', 'islemtarih', 'decimalfield']

    fields = (('isim', 'soyisim'), 'sehir', ('coklusec', 'aylar'))

    ### request e göre fields gösterim koşulları
    def get_fields(self, request, obj=None):
        print('------------>  Zaman: {}  .--> Def: {} <------------'.format(datetime.now(), inspect.stack()[0][3]))
        print('Çağıran: {}:{}, Fonksiyon:'.format(inspect.stack()[1][1], inspect.stack()[1][2]), inspect.stack()[1][3])

        print(request.user.username, request.user.is_superuser)

        _fields = self.fields

        if request.user.username == 'admin':
            _fields = (('isim', 'soyisim'), 'sehir', ('coklusec', 'aylar'), 'yazar')

        if request.user.username == 'muslu':
            _fields = (('isim', 'soyisim', 'sehir', 'decimalfield'), ('coklusec', 'aylar'), 'yazar')

        if request.user.is_superuser:
            _fields = (('isim', 'soyisim', 'sehir', 'decimalfield', 'coklusec', 'aylar'), 'yazar')

        ## Kayıt düzenleniyor ise
        if obj:
            _fields = (('isim', 'soyisim', 'sehir'), 'yazar')

        return _fields
