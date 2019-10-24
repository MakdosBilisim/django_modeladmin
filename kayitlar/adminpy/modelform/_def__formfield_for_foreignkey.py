import inspect
from datetime import datetime

from django.contrib import admin

from kayitlar.models import Kullanicilar, Aylar


@admin.register(Kullanicilar)
class KullanicilarAdmin(admin.ModelAdmin):
    list_display = ['isim', 'soyisim', 'aylar']

    ## foreignkey leri otomatik doldurma, içerikleri yetkilendirme
    def formfield_for_foreignkey(self, db_field, request=None, **kwargs):
        print('------------>  Zaman: {}  .--> Def: {} <------------'.format(datetime.now(), inspect.stack()[0][3]))
        print('Çağıran: {}:{}, Fonksiyon:'.format(inspect.stack()[1][1], inspect.stack()[1][2]), inspect.stack()[1][3])

        gecerli_url = request.META['PATH_INFO']

        ## İlk kayıt sayfası ise
        if gecerli_url.endswith('/add/'):
            print('kayıt eklenirken')
        else:
            print('Kayıt düzenlenirken')

        ## Yazar alanını otomatik olarak giriş yapan kullanıcıyı seç
        if db_field.name == 'yazar':
            ## initial ile otomatik seçim yaptır.
            kwargs['initial'] = request.user.id

            return db_field.formfield(**kwargs)

        ## Aylar alanında admin sadece O ile başlayan kayıtları görsün, diğer kullanıcılar tüm kayıtları
        if db_field.name == 'aylar':
            if request.user.username == 'admin':
                kwargs['queryset'] = Aylar.objects.filter(ay_ismi__startswith='O')

        kwargs['empty_label'] = 'Seçim yapılmadı!!'

        if request.user.username == 'admin':
            kwargs['label'] = 'Burayı admin harici görebilir'

        if db_field.name == 'aylar':
            # if request.user.username != 'admin':
            from django.forms import Select
            # kwargs['widget'] = Select(attrs={'disabled': 'true'})
            kwargs['widget'] = Select(attrs={'class': 'OzelCLASS', 'data-toggle': 'OZELDATA'})

        return super().formfield_for_foreignkey(db_field, request, **kwargs)
