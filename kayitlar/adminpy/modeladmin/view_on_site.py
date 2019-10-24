from django.contrib import admin

from kayitlar.models import Kullanicilar


@admin.register(Kullanicilar)
class KullanicilarAdmin(admin.ModelAdmin):
    view_on_site = True ## Kayıt düzenleme sayfasında SİTEDE GÖRÜNTÜLE butonu getirir
    def view_on_site(self, obj):
        from django.urls import reverse
        ### urls.py ye detay fonksiyonu eklenmeli
        #### urlpatterns += [path('detaygoster/<int:id>/', detay, name='detay'),]

        url = reverse('detay', kwargs={'id': obj.id})
        return url
        # return 'https://makdos.com' + url
