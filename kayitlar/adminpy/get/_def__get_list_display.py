from django.contrib import admin

from kayitlar.models import Kullanicilar


@admin.register(Kullanicilar)
class KullanicilarAdmin(admin.ModelAdmin):
    # list_display = ['isim', 'soyisim', 'aylar', 'sehir', 'decimalfield']

    ## Kullanıcıya özel list_display koşulları
    def get_list_display(self, request):

        if request.user.username == 'admin':
            self.list_display = ['isim', 'soyisim', 'aylar']
        elif request.user.username == 'muslu':
            self.list_display = ['isim', 'aylar']
        else:  ## Default yazılmadıysa diğer tüm koşullara uyanlara gösterilecek
            self.list_display = ['isim', 'soyisim', 'aylar', 'sehir', 'decimalfield']

        return self.list_display
