import inspect
from datetime import datetime

from django.contrib import admin

from kayitlar.models import Kullanicilar


def mail_gonder(kullanici, mesaj):
    import smtplib

    from email.mime.multipart import MIMEMultipart
    from email.mime.text import MIMEText

    gonderen = "musluyuksektepe@gmail.com"
    alici = "yuksektepemurat@gmail.com"

    msg = MIMEMultipart('alternative')
    msg['Subject'] = "Kayıt Silindi"
    msg['From'] = gonderen
    msg['To'] = alici

    html = """ <html><head></head><body>
        <p>
            {} kullanıcısı <b>{}</b> kaydını sildi!
        </p>
      </body></html>""".format(kullanici, mesaj)

    part2 = MIMEText(html, 'html')
    msg.attach(part2)

    mail = smtplib.SMTP('smtp.gmail.com', 587)
    mail.ehlo()
    mail.starttls()
    mail.login('musluyuksektepe@gmail.com', '')
    mail.sendmail(gonderen, alici, msg.as_string())
    mail.quit()


@admin.register(Kullanicilar)
class KullanicilarAdmin(admin.ModelAdmin):
    list_display = ['isim', 'soyisim', 'aylar']

    ## Kayıt silme sorusu anında çağrılır.
    def delete_view(self, request, object_id, extra_context=None):
        print('------------>  Zaman: {}  .--> Def: {} <------------'.format(datetime.now(), inspect.stack()[0][3]))
        print('Çağıran: {}:{}, Fonksiyon:'.format(inspect.stack()[1][1], inspect.stack()[1][2]), inspect.stack()[1][3])

        print(request.user.username)
        print(object_id)

        return super().delete_view(request, object_id, extra_context)

    ## Kayıt kesin silindikten sonra  delete_view sonrası çağrılır.
    def response_delete(self, request, obj_display, obj_id):
        print('------------>  Zaman: {}  .--> Def: {} <------------'.format(datetime.now(), inspect.stack()[0][3]))
        print('Çağıran: {}:{}, Fonksiyon:'.format(inspect.stack()[1][1], inspect.stack()[1][2]), inspect.stack()[1][3])

        # print(request.user.username)

        ## models.py class Kullanicilar __str__ de yazan bilgileri döndürür.
        print(obj_display)

        # mail_gonder(request.user.username, obj_display)

        ## Kullanıcıya mesaj göstermek
        from django.contrib import messages

        ## Mesaj içeriğinde HTML etiketleri kullan
        from django.utils.safestring import mark_safe

        messages.warning(request, mark_safe('DİKKAT: Silinen kayıt (<b>{}</b>) mail olarak gönderildi!'.format(obj_display)))

        return super().response_delete(request, obj_display, obj_id)
