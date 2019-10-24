import inspect
from datetime import datetime

from django.contrib import admin

from kayitlar.models import Kullanicilar


@admin.register(Kullanicilar)
class KullanicilarAdmin(admin.ModelAdmin):
    list_display = ['isim', 'soyisim', 'islemtarih']

    ## python3.6/site-packages/django/contrib/admin/templates/admin/change_form.html

    ## Kayıt düzenleme sırasında oluşan forma ve verilere müdahale etmek

    ## def add_view ile aynı işlemler yapılabilir. Ayrıca; Düzenlenen kaydın id si hazır verilir.
    def change_view(self, request, object_id, form_url='', extra_context=None):
        print('------------>  Zaman: {}  .--> Def: {} <------------'.format(datetime.now(), inspect.stack()[0][3]))

        ## Sayfadaki giriş yapan kullanıcı
        print(request.user)
        print(object_id)

        ## Düzenleme öncesi var olan kayıt bilgilerine ulaşmak
        kayit_bul = self.model.objects.get(id=object_id)

        ## Kayda ait son islemtarih bilgisi
        sonduzenleme_tarih = kayit_bul.islemtarih.strftime('%d %B %Y (%a) %H:%M:%S')

        ## Kullanıcıya mesaj göstermek
        from django.contrib import messages

        ## Mesaj içeriğinde HTML etiketleri kullan
        from django.utils.safestring import mark_safe

        ## NOT: Son düzenleme için DateTimeField kayıt sonrası güncellenmledi. models.py save methoduna super save().. öncesine self.islemtarih = datetime.now() eklenmeli.
        messages.warning(request, mark_safe('Bu kayıt en sonra <b style="color:red;">{}</b> tarihinde güncellendi.'.format(sonduzenleme_tarih)))

        ## Kayıt öncesi butonları gizle/göster
        extra_context = extra_context or {}
        extra_context['show_save_and_continue'] = True

        #### Güncelleme öncesi eski ve yeni değerlere ulaşmak
        eski_deger = kayit_bul.isim

        degisiklik = super().change_view(request, object_id, form_url, extra_context)

        kayit_bul = self.model.objects.get(id=object_id)
        yeni_kayit = kayit_bul.isim

        return degisiklik
