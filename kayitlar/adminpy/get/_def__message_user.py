import inspect
from datetime import datetime

from django.contrib import admin, messages

from kayitlar.models import Kullanicilar


def mail_gonder(kullanici, mesaj, url):
    import smtplib

    from email.mime.multipart import MIMEMultipart
    from email.mime.text import MIMEText

    gonderen = "musluyuksektepe@gmail.com"
    alici = "yuksektepemurat@gmail.com"

    msg = MIMEMultipart('alternative')
    msg['Subject'] = "Özel Mesaj gösterildi"
    msg['From'] = gonderen
    msg['To'] = alici

    html = """ <html><head></head><body>
        <p>
        {} kullanıcısına {} yolunda <b>{}</b> mesajı gösterildi.
        </p>
      </body></html>""".format(kullanici, url, mesaj)

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
    search_fields = ['soyisim']

    ## Kullanıcılara özel mesaj gönderirken rapor almak ve loglamak.
    def message_user(self, request, message, level=messages.INFO, extra_tags='', fail_silently=False):
        # print(request.user.username)
        print('------------>  Zaman: {}  .--> Def: {} <------------'.format(datetime.now(), inspect.stack()[0][3]))
        print('Çağıran: {}:{}, Fonksiyon:'.format(inspect.stack()[1][1], inspect.stack()[1][2]), inspect.stack()[1][3])

        ## İşlem yapılan yol
        print(request.path)

        ## URL ye ait parametreler. Örn: arama yapılırken aranan kelime gibi
        for parametre in request.GET.items():
            print(parametre)

        ## Mesaj
        print(message)
        print(level)
        print(extra_tags)

        mail_gonder(request.user.username, message, request.path)

        messages.add_message(request, level, message, extra_tags=extra_tags, fail_silently=fail_silently)

    def get_search_results(self, request, queryset, search_term):
        queryset, use_distinct = super().get_search_results(request, queryset, search_term)
        aranan = search_term.strip()
        if not aranan:
            return queryset, use_distinct

        queryset |= self.model.objects.filter(isim__startswith=aranan)

        self.message_user(request, 'self.message_user ile gönderildi', level=messages.INFO)

        return queryset, use_distinct
