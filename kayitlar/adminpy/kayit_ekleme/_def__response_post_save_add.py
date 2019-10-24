import inspect
from datetime import datetime

from django.contrib import admin

from kayitlar.models import Kullanicilar


@admin.register(Kullanicilar)
class KullanicilarAdmin(admin.ModelAdmin):
    list_display = ['isim', 'soyisim', 'aylar']

    def add_view(self, request, form_url='', extra_context=None):
        print('------------>  Zaman: {}  .--> Def: {} <------------'.format(datetime.now(), inspect.stack()[0][3]))
        print('Çağıran: {}:{}, Fonksiyon:'.format(inspect.stack()[1][1], inspect.stack()[1][2]), inspect.stack()[1][3])
        return super().add_view(request, form_url, extra_context)

    ## Kayıt ekleme sonrası işlem yaptırmak
    def response_add(self, request, obj, post_url_continue=None):
        print('------------>  Zaman: {}  .--> Def: {} <------------'.format(datetime.now(), inspect.stack()[0][3]))
        print('Çağıran: {}:{}, Fonksiyon:'.format(inspect.stack()[1][1], inspect.stack()[1][2]), inspect.stack()[1][3])

        return super().response_add(request, obj, post_url_continue)

    ## Yeni kayıt oluştururken 'Kaydet' düğmesine basıldıktan sonra çağrılır.
    def response_post_save_add(self, request, obj):
        # print(request.user.username)
        print('------------>  Zaman: {}  .--> Def: {} <------------'.format(datetime.now(), inspect.stack()[0][3]))
        print('Çağıran: {}:{}, Fonksiyon:'.format(inspect.stack()[1][1], inspect.stack()[1][2]), inspect.stack()[1][3])

        obj.isim = 'asdasdasdasd'
        obj.save()
        return self._response_post_save(request, obj)

