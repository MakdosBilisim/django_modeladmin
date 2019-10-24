import inspect
from datetime import datetime

from django.contrib import admin

from kayitlar.models import Kullanicilar


@admin.register(Kullanicilar)
class KullanicilarAdmin(admin.ModelAdmin):
    list_display = ['isim', 'soyisim', 'aylar']

    ## Sadece belirli kullanıcılar kayıt silebilir.
    def has_delete_permission(self, request, obj=None):

        # print(request.user.username)
        print('------------>  Zaman: {}  .--> Def: {} <------------'.format(datetime.now(), inspect.stack()[0][3]))
        print('Çağıran: {}:{}, Fonksiyon:'.format(inspect.stack()[1][1], inspect.stack()[1][2]), inspect.stack()[1][3])

        if obj is None:
            return False

        gecerli_ay = datetime.now().strftime("%B")

        if obj.aylar.ay_ismi == gecerli_ay:
            ## Kullanıcıya mesaj göstermek
            from django.contrib import messages

            ## Mesaj içeriğinde HTML etiketleri kullan
            from django.utils.safestring import mark_safe

            messages.error(request, mark_safe('{} ayına ait kayıtlar silinemez!'.format(gecerli_ay)))

            return False

        if request.user.is_superuser:
            return True
        elif request.user == obj.isim:
            return True
        else:
            return False
