import calendar

from django.contrib.auth.models import User
from django.db import models
from django.utils.safestring import mark_safe

SEHIRLER = (
    ('adana', 'Adana'),
    ('izmir', 'İzmir'),
    ('istanbul', 'İstanbul'),
)

###################################################################################
### locale -a ile var olan diller öğrenilmeli
import locale

locale.setlocale(locale.LC_ALL, 'tr_TR.utf8')


# locale.setlocale(locale.LC_ALL, 'de_AT.utf8')


class CokluManytoMany(models.Model):
    secimler = models.CharField(verbose_name='Çoklu Seçim', max_length=15)

    def __str__(self):
        return self.secimler

    class Meta:
        verbose_name = 'Seçim'
        verbose_name_plural = 'Çoklu Seçim - M2M'


class Aylar(models.Model):
    ay_ismi = models.CharField(verbose_name='Ay İsimleri', choices=[(str(calendar.month_name[i]), calendar.month_name[i]) for i in range(1, 13)], max_length=15)

    def __str__(self):
        return self.ay_ismi  ## Kullanılmaz ise bir yerde kayıt görüntülendiğinde (Örn: foreingkey model adı object(1) gibi gösterilir.)
        # return self.get_ay_ismi_display()  ## Seçilen choices alanın değerini gösterir. Örneğin: Ağustos

    ###################################################################################
    ### Meta sınıfı kullanılmaz ise
    # class Meta:
    #     verbose_name = 'Ay' # Kayıt eklerken model adı küçük harf ile gösterilir.
    #     verbose_name_plural = 'Ayların İsimleri' Model adı s ile biter.
    ###################################################################################

    def save(self, *args, **kwargs):
        for arg in args:
            print(arg)
        for key, value in kwargs.items():
            print("%s == %s" % (key, value))
        super().save(*args, **kwargs)  ## Unutulmamalı.


class Kullanicilar(models.Model):
    yazar = models.ForeignKey(User, on_delete=models.CASCADE, verbose_name='Yazar', blank=True, null=True)
    aylar = models.ForeignKey(Aylar, on_delete=models.CASCADE, verbose_name='Aylar', default=1, blank=True, null=True)
    coklusec = models.ManyToManyField(CokluManytoMany, verbose_name='Çoklu Seçim M2M')
    sehir = models.CharField('Şehir', max_length=30, choices=SEHIRLER, default='adana')
    isim = models.CharField(max_length=30, verbose_name='İsim', help_text='Max: 30 karakter')
    soyisim = models.CharField(max_length=60, verbose_name='Soyisim', help_text='Max: 60 karakter')
    decimalfield = models.DecimalField(max_digits=8, decimal_places=2, null=True, blank=True)
    islemtarih = models.DateTimeField(verbose_name='Tarih/Saat', auto_now_add=True)
    toplantitarih = models.DateTimeField(verbose_name='Toplantı Tarihi', null=True, blank=True)
    gorsel = models.ImageField(upload_to='yuklenenler', blank=True, null=True)

    def __str__(self):
        return '{} {} --> {}'.format(self.isim, self.soyisim, self.islemtarih)

    def __html__(self):
        return mark_safe('<span style="color: red">{} {}</span>'.format(self.isim, self.soyisim))

    # def unique_error_message(self, model_class, unique_check):
    #     if model_class == type(self) and unique_check == ('isim', 'soyisim'):
    #         kim = model_class.objects.get(isim=self.isim, soyisim=self.soyisim)
    #         return mark_safe('<span style="color: black; font-size:32px;">{} {} (ID: <b>{}</b>) zaten tanımlandı!</span><br/>'.format(self.isim, self.soyisim, kim.id))
    #     else:
    #         return super().unique_error_message(model_class, unique_check)

    class Meta:
        verbose_name = 'Kullanıcı'
        verbose_name_plural = 'Kullanıcılar'
        # unique_together = ['isim', 'soyisim']

    # def save(self, ozel_bilgi={}, *args, **kwargs):
    #
    #     print("~~~~~> models.py save()")
    #     print('~~~~~> models.py  Zaman: {}  .--> Def: {} <------------'.format(datetime.now(), inspect.stack()[0][3]))
    #     print('~~~~~> models.py {}'.format(self.isim))
    #     super().save(*args, **kwargs)
    #     print("~~~~~> models.py save()")

    #     ###################################################################################
    #     print("===========Argümanlar===========")
    #     # for arg in args:
    #     #     print(arg)
    #
    #     # print(ozel_bilgi.get('ozel_durum'))
    #     print(ozel_bilgi.get('kayit_eden'))  ##<class 'django.utils.functional.SimpleLazyObject'>
    #
    #     print("=+=========Argümanlar=========+=")
    #     ###################################################################################
    #     print("===========save===========")
    #     print(self.isim)
    #
    #     if str(ozel_bilgi.get('kayit_eden')) == 'murat':
    #         print('Murat artık kayıt girişi yapamaz!!')
    #         return
    #
    #     if self.isim == 'Muslu':
    #         print("isim Muslu olmaz!")
    #         return
    #
    #     print("super().save öncesi")
    #
    #     if not self.isim.istitle():
    #         self.isim = self.isim.title()
    #         print('İsmin ilk harfi büyük harf yapıldı!')
    #
    #     self.soyisim = self.soyisim.upper()
    #
    #     ## Her kayıtta islemtarihi alanını otomatik güncelle
    #     self.islemtarih = datetime.now()
    #
    #     super().save(*args, **kwargs)
    #     print('Kayıt edildi!')
    #     print("super().save sonrası")
    #     print(self.isim)
    #     print("=+=========save=========+=")


class KullanicilaraAitInlineModel(models.Model):
    kullanicilar = models.ForeignKey(Kullanicilar, on_delete=models.CASCADE, verbose_name='Kullanıcılar')
    charfield = models.CharField(max_length=80, verbose_name='Charfield', default=None)
    integerfield = models.SmallIntegerField(verbose_name='SmalIntegerfield', default=0)

    def __str__(self):
        return self.charfield

    class Meta:
        verbose_name = 'Inline'
        verbose_name_plural = 'Örnek INline'
