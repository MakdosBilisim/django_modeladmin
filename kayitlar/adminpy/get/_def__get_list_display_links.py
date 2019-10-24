from django.contrib import admin

from kayitlar.models import Kullanicilar


@admin.register(Kullanicilar)
class KullanicilarAdmin(admin.ModelAdmin):
    list_display = ['isim', 'soyisim', 'sehir']
    list_display_links = ['isim', 'soyisim']

    ## Kullanıcıya göre list_display deki alanlarda kayıt düzenleme sayfına link vermek.
    def get_list_display_links(self, request, list_display):

        # print(list_display)

        ## Eğer list_display da olmayan alanlar yazılırsa yalnızca ortak olanlara link verilir.
        if request.user.username == 'admin':
            self.list_display_links = ['isim', 'soyisim', 'aylar']
        elif request.user.username == 'muslu':
            self.list_display_links = ['isim', 'aylar']
        else:  ## Diğer kullanıcılar
            self.list_display_links = ['isim', 'soyisim', 'aylar', 'sehir', 'decimalfield']

        return self.list_display_links
