from django.contrib import admin

from kayitlar.models import Kullanicilar


@admin.register(Kullanicilar)
class KullanicilarAdmin(admin.ModelAdmin):
    list_display = ['isim', 'soyisim', 'aylar']

    ## Eylemler (Toplu işlemler) için koşullar
    def get_actions(self, request):
        actions = super().get_actions(request)

        ## Bir kayıt veya hiç kayıt yok ise Eylemler açılır kutusunu gösterme
        # if self.model.objects.count() <= 1:
        #     del actions['delete_selected']

        ## muslu kullanıcısı eylemler açılır kutusunu görüntüleyemez.
        if request.user.username == 'muslu':
            del actions['delete_selected']

        return actions
