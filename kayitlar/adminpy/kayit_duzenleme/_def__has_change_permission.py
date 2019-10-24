import inspect
from datetime import datetime

from django.contrib import admin

from kayitlar.models import Kullanicilar


@admin.register(Kullanicilar)
class KullanicilarAdmin(admin.ModelAdmin):
    list_display = ['isim', 'soyisim', 'aylar']

    ## Sadece belirli kullanıcılar kayıt güncelleyebilir.
    def has_change_permission(self, request, obj=None):

        # print(request.user.username)
        print('------------>  Zaman: {}  .--> Def: {} <------------'.format(datetime.now(), inspect.stack()[0][3]))
        print('Çağıran: {}:{}, Fonksiyon:'.format(inspect.stack()[1][1], inspect.stack()[1][2]), inspect.stack()[1][3])

        if obj is None:
            return False

        # print(obj.id)

        if request.user.is_superuser:
            return True
        elif request.user == obj.isim:
            return True
        else:
            return False
