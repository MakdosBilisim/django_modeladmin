import inspect
from datetime import datetime

from django.contrib import admin

from kayitlar.models import Kullanicilar


@admin.register(Kullanicilar)
class KullanicilarAdmin(admin.ModelAdmin):
    list_display = ['isim', 'soyisim', 'aylar']

    ## Kayıt sayfasına girince ve kayıt sonrası çağrılır
    def change_view(self, request, object_id, form_url='', extra_context=None):
        print('------------>  Zaman: {}  .--> Def: {} <------------'.format(datetime.now(), inspect.stack()[0][3]))
        print('Çağıran: {}:{}, Fonksiyon:'.format(inspect.stack()[1][1], inspect.stack()[1][2]), inspect.stack()[1][3])

        return super().change_view(request, object_id, form_url, extra_context)

    ## Kayıt güncelleme sonrası change_view den sonra çağrılır
    def response_change(self, request, obj, post_url_continue=None):
        print('------------>  Zaman: {}  .--> Def: {} <------------'.format(datetime.now(), inspect.stack()[0][3]))
        print('Çağıran: {}:{}, Fonksiyon:'.format(inspect.stack()[1][1], inspect.stack()[1][2]), inspect.stack()[1][3])

        obj.isim = obj.isim.lower()
        obj.save()

        return self.response_post_save_change(request, obj)

    ## Varolan bir kaydı düzenlerken 'Kaydet' düğmesine basıldıktan sonra çağrılır.
    ## En son kaydı değiştiren yer
    def response_post_save_change(self, request, obj):
        # print(request.user.username)
        print('------------>  Zaman: {}  .--> Def: {} <------------'.format(datetime.now(), inspect.stack()[0][3]))
        print('Çağıran: {}:{}, Fonksiyon:'.format(inspect.stack()[1][1], inspect.stack()[1][2]), inspect.stack()[1][3])

        obj.isim = 'asdasdasdasd'
        obj.save()
        return self._response_post_save(request, obj)
