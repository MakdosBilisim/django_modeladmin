import inspect
from datetime import datetime

from django.contrib import admin
from django.contrib.admin.utils import model_format_dict
from django.db.models import BLANK_CHOICE_DASH

from kayitlar.models import Kullanicilar


@admin.register(Kullanicilar)
class KullanicilarAdmin(admin.ModelAdmin):
    list_display = ['isim', 'soyisim', 'aylar']

    # # Action
    def action_ornek(modeladmin, request, queryset):
        for kayit in queryset:
            kayit.isim = kayit.isim.lower()
            kayit.save()
        return queryset

    def action_ornek2(modeladmin, request, queryset):
        for kayit in queryset:
            kayit.soyisim = kayit.soyisim.upper()
            kayit.save()
        return queryset

    actions = [action_ornek, action_ornek2]

    ## Eylemler (Toplu işlemler) için koşullar
    def get_actions(self, request):
        actions = super().get_actions(request)
        if request.user.username == 'admin':
            del actions['delete_selected']
        return actions

    ## get_actions dan dönen yetkilere göre eylemler seçeneklerinin düzenlenmesi
    def get_action_choices(self, request, default_choices=BLANK_CHOICE_DASH):
        # print(request.user.username)
        print('------------>  Zaman: {}  .--> Def: {} <------------'.format(datetime.now(), inspect.stack()[0][3]))
        print('Çağıran: {}:{}, Fonksiyon:'.format(inspect.stack()[1][1], inspect.stack()[1][2]), inspect.stack()[1][3])

        ## secimlerin içeriğini boşalt, sadece ---- olan seçim kalsın
        secimler = [] + default_choices

        for fonksiyon, isim, aciklama in self.get_actions(request).values():
            secim = [isim, aciklama % model_format_dict(self.opts)]

            if secim[0] == 'action_ornek2':
                secim[1] = 'Soyisimleri BÜYÜK harfe çevir'

            if secim[0] == 'action_ornek':
                secim[1] = 'İsimleri küçük harfe çevir'

            secimler.append(secim)

            ## Çoklu koşula göre listeden çıkartmak
            ## kullanıcı admin ise 2 seçimi de gizle
            # if (request.user.username == 'admin') and (secim[0] == 'action_ornek' or secim[0] == 'action_ornek2'):
            # if request.user.username == 'admin' and secim[0] == 'action_ornek':
            #     secimler.remove(secim)

        return secimler
