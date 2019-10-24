import inspect
from datetime import datetime

from django.contrib import admin

from kayitlar.models import Kullanicilar


def mail_gonder(silinen_kayit_id):
    import smtplib

    from email.mime.multipart import MIMEMultipart
    from email.mime.text import MIMEText

    gonderen = "musluyuksektepe@gmail.com"
    alici = "yuksektepemurat@gmail.com"

    msg = MIMEMultipart('alternative')
    msg['Subject'] = "Kayıt Silinmesi"
    msg['From'] = gonderen
    msg['To'] = alici

    html = """\
    <html>
      <head></head>
      <body>
        <p>Merhaba!
        <br/>
        {} nolu kayıt silindi!
        </p>
      </body>
    </html>
    """.format(silinen_kayit_id)

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

    ## get_delete_objects gibi ama kayıt kesin silinirse bilgi verir.
    def delete_model(self, request, obj):
        # print(request.user.username)
        print('------------>  Zaman: {}  .--> Def: {} <------------'.format(datetime.now(), inspect.stack()[0][3]))
        print('Çağıran: {}:{}, Fonksiyon:'.format(inspect.stack()[1][1], inspect.stack()[1][2]), inspect.stack()[1][3])

        mail_gonder(obj.id)
