import inspect
from datetime import datetime

from django.contrib import admin

from kayitlar.models import Kullanicilar, Aylar


@admin.register(Kullanicilar)
class KullanicilarAdmin(admin.ModelAdmin):
    list_display = ['isim', 'soyisim', 'aylar']


    ### Adım adım kayıt
    fieldsets = [
        ('Önce Gösterilecekler', {'classes': ('wide', 'collapse'), 'fields': ('sehir', 'decimalfield',)}),
        ('Sonraki Sayfa Üst', {'classes': ('wide',), 'fields': ('coklusec', 'aylar',)}),
        ('Sonraki Sayfa Alt', {'classes': ('wide', 'collapse'), 'fields': ('isim', 'soyisim',)}),
    ]

    add_fieldsets = [
        ('Önce Gösterilecekler', {'fields': ('sehir', 'decimalfield',)}),
    ]

    ## Kayıt yapılırken önce bazı alanları sonra diğer alanları göster.
    ## İlk girilen alan değerlerine göre otomatik tamamlama yapılabilir.
    def get_fieldsets(self, request, obj=None):
        print('------------>  Zaman: {}  .--> Def: {} <------------'.format(datetime.now(), inspect.stack()[0][3]))
        print('Çağıran: {}:{}, Fonksiyon:'.format(inspect.stack()[1][1], inspect.stack()[1][2]), inspect.stack()[1][3])

        if not obj:
            return self.add_fieldsets
        else:

            if obj.sehir == 'izmir':
                obj.isim = 'Önceki sayfada şehir İzmir seçildi'
                obj.aylar = Aylar.objects.get(ay_ismi='Şubat')

            return self.fieldsets

        return super().get_fieldsets(request, obj)

    ## Kayıt sonrası işlemler
    def response_add(self, request, obj, post_url_continue=None):
        print('------------>  Zaman: {}  .--> Def: {} <------------'.format(datetime.now(), inspect.stack()[0][3]))
        print('Çağıran: {}:{}, Fonksiyon:'.format(inspect.stack()[1][1], inspect.stack()[1][2]), inspect.stack()[1][3])

        ## Kaydet ve yeni ekleme butonuna veya Kaydet basılsa bile kayda devam ettir.
        if '_addanother' in request.POST or '_save' in request.POST:
            # if '_addanother' in request.POST and IS_POPUP_VAR not in request.POST:
            request.POST = request.POST.copy()
            request.POST['_continue'] = 1
        return super().response_add(request, obj, post_url_continue)
