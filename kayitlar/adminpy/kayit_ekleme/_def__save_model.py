import inspect
from datetime import datetime

from django.contrib import admin

from kayitlar.models import Kullanicilar


@admin.register(Kullanicilar)
class KullanicilarAdmin(admin.ModelAdmin):
    list_display = ['isim', 'soyisim', 'islemtarih', 'karakod_goster']

    def karakod_goster(self, obj):
        from django.utils.safestring import mark_safe
        return mark_safe('<img style="width:100px" src="{}" />'.format(obj.gorsel.url))

    karakod_goster.admin_order_field = 'gorsel'
    karakod_goster.short_description = 'Kare Kod'

    def save_model(self, request, obj, form, change):
        print("~~~~~> admin.py save_model()")

        print('------------>  Zaman: {}  .--> Def: {} <------------'.format(datetime.now(), inspect.stack()[0][3]))
        print('Çağıran: {}:{}, Fonksiyon:'.format(inspect.stack()[1][1], inspect.stack()[1][2]), inspect.stack()[1][3])

        print("~~~~~> admin.py ====> Kayıt Öncesi <====")

        ## request ile sayfadaki kullanıcı bilgileri
        # print(request.user)

        ## Kayıt formunun HTML hali
        # print(form)

        ## Kayıt yeni mi güncelleme mi?
        # if change:
        #     print("~~~~~> admin.py Kayıt güncellendi")
        # else:
        #     print("~~~~~> admin.py Kayıt ilk defa girildi")

        ## Var olan kayıt
        # print('~~~~~> admin.py Var olan kayıt: {}'.format(obj.isim))
        ## Yeni içerik
        # obj.isim = 'Yeni isim'
        # print('~~~~~> admin.py Yeni içerik: {}'.format(obj.isim))

        ## Değişiklik yapılıp/yapılmadığı hakkında bilgi ver
        # from django.contrib import messages
        # if 'isim' in form.changed_data:
        #     messages.info(request, "İsim alanı güncellendi")
        # else:
        #     messages.info(request, "İsim alanında değişiklik yapılmadı!")

        if change:
            ## Kayıt öncesi geçerli değer
            guncel_isim = self.model.objects.get(id=obj.id).isim
            print("~~~~~> admin.py guncel_isim: {}".format(guncel_isim))

            import os
            os.remove(obj.gorsel.path)

        else:
            guncel_isim = ''

        super().save_model(request, obj, form, change)

        ## Kayıt sonrası güncellenen değer
        yeni_isim = obj.isim

        print("~~~~~> admin.py yeni_isim: {}".format(yeni_isim))

        if yeni_isim != guncel_isim:
            ## Kayıt sonrası QR kod oluştur ve list_display de göster
            import qrcode
            qr = qrcode.QRCode(box_size=10, border=4)
            qr.add_data(obj.isim)
            qr.make(fit=True)
            img = qr.make_image()

            from django.conf import settings
            gorsel_gecici_yol = '{}yuklenenler/{}.jpg'.format(settings.MEDIA_ROOT, obj.isim)

            img.save(gorsel_gecici_yol)

            from django.core.files import File
            obj.gorsel.save('{}.png'.format(obj.isim), File(open(gorsel_gecici_yol, 'rb')))

            ## Geçici dosyayı sil.
            import os
            os.remove(gorsel_gecici_yol)

            # Kayıt sonrası QR kod oluştur ve list_display de göster

        print("~~~~~> admin.py ====> Kayıt Sonrası <====")

        ## Kayıt sonrası yeni içerik
        # print('~~~~~> admin.py Kayıt Edildi. Yeni içerik: {}'.format(obj.isim))

        print("~~~~~> admin.py save_model()")