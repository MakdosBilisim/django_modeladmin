import inspect
from datetime import datetime

from django.contrib import admin

from kayitlar.models import Kullanicilar


@admin.register(Kullanicilar)
class KullanicilarAdmin(admin.ModelAdmin):
    list_display = ['isim', 'soyisim', 'aylar']

    ## Sadece belirli kullanıcılar kayıt ekleyebilir.
    def has_add_permission(self, request):
        # print(request.user.username)

        print('------------>  Zaman: {}  .--> Def: {} <------------'.format(datetime.now(), inspect.stack()[0][3]))
        print('Çağıran: {}:{}, Fonksiyon:'.format(inspect.stack()[1][1], inspect.stack()[1][2]), inspect.stack()[1][3])

        if request.user.username == 'admin':
            return True
        else:

            ## Kullanıcıya mesaj göstermek
            from django.contrib import messages

            ## Mesaj içeriğinde HTML etiketleri kullan
            from django.utils.safestring import mark_safe

            messages.error(request, mark_safe('Kayıt girmek için yetkiniz bulunmuyor!'))

            return False
