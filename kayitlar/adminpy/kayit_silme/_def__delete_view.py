import inspect
from datetime import datetime

from django.contrib import admin

from kayitlar.models import Kullanicilar


@admin.register(Kullanicilar)
class KullanicilarAdmin(admin.ModelAdmin):
    list_display = ['isim', 'soyisim', 'islemtarih']

    ## python3.6/site-packages/django/contrib/admin/templates/admin/delete_confirmation.html

    ## Kayıt silme

    def delete_view(self, request, object_id, extra_context=None):
        print('------------>  Zaman: {}  .--> Def: {} <------------'.format(datetime.now(), inspect.stack()[0][3]))

        ## Sayfadaki giriş yapan kullanıcı
        print(request.user)
        print(object_id)

        ## Düzenleme öncesi var olan kayıt bilgilerine ulaşmak
        kayit_bul = self.model.objects.get(id=object_id)

        ## Kayda ait son islemtarih bilgisi
        sonduzenleme_tarih = kayit_bul.islemtarih.strftime('%d %B %Y (%a) %H:%M:%S')

        from django.urls import reverse
        gecmisizleme_linki = reverse("admin:%s_%s_history" % (self.model._meta.app_label, self.model._meta.model_name), args=(object_id,))

        # print(gecmisizleme_linki)

        ## Kullanıcıya mesaj göstermek
        from django.contrib import messages

        ## Mesaj içeriğinde HTML etiketleri kullan
        from django.utils.safestring import mark_safe

        ## NOT: Son düzenleme için DateTimeField kayıt sonrası güncellenmledi. models.py save methoduna super save().. öncesine self.islemtarih = datetime.now() eklenmeli.
        messages.warning(request, mark_safe('Bu kayıtın <b>geçmiş</b> işlemlerini <b>ayrı sayfada</b> görmek için <a href="{}" target=_blank><b>burayı</b></a> tıklayın.'.format(gecmisizleme_linki)))

        return super().delete_view(request, object_id, extra_context)
