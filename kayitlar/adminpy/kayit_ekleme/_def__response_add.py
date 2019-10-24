import inspect
from datetime import datetime

from django.contrib import admin
from django.http import HttpResponseRedirect

from kayitlar.models import Kullanicilar


@admin.register(Kullanicilar)
class KullanicilarAdmin(admin.ModelAdmin):
    list_display = ['isim', 'soyisim', 'aylar']

    ## Kayıt ekleme sonrası işlem yaptırmak
    def response_add(self, request, obj, post_url_continue=None):
        print('------------>  Zaman: {}  .--> Def: {} <------------'.format(datetime.now(), inspect.stack()[0][3]))
        print('Çağıran: {}:{}, Fonksiyon:'.format(inspect.stack()[1][1], inspect.stack()[1][2]), inspect.stack()[1][3])

        ## Kayıt sonrası, kaydet ve düzenlemeye devam et tıklanmaz ise başka bir modelin sayfasına yönlendir.
        if '_continue' not in request.POST:
            return HttpResponseRedirect('/admin/kayitlar/digermodel/')
        else:
            return super().response_add(request, obj, post_url_continue)

        ## Kayıt yap ve aynı sayfada kal
        # from django.contrib.admin.options import IS_POPUP_VAR
        # if '_addanother' not in request.POST and IS_POPUP_VAR not in request.POST:
        #     request.POST = request.POST.copy()
        #     request.POST['_continue'] = 1
        # return super().response_add(request, obj, post_url_continue)
