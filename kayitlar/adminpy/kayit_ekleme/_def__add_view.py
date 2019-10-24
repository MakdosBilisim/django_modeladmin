import inspect
from datetime import datetime

from django.contrib import admin

from kayitlar.models import Kullanicilar


@admin.register(Kullanicilar)
class KullanicilarAdmin(admin.ModelAdmin):
    list_display = ['isim', 'soyisim', 'islemtarih']

    ## python3.6/site-packages/django/contrib/admin/templates/admin/change_form.html
    def add_view(self, request, form_url='', extra_context=None):
        print('------------>  Zaman: {}  .--> Def: {} <------------'.format(datetime.now(), inspect.stack()[0][3]))
        print('Çağıran: {}:{}, Fonksiyon:'.format(inspect.stack()[1][1], inspect.stack()[1][2]), inspect.stack()[1][3])

        ## Sayfadaki giriş yapan kullanıcı
        print(request.user)

        ## Bu modeldeki son kayıt bilgileri. ÖRn: son kayıt ID
        sonID = self.model.objects.last().id

        ## Kayıt öncesi tüm  GET ile gelen form bilgilerini kopyala
        data = request.GET.copy()

        ## Giriş yapan kullanıcı admin ise
        if str(request.user) == "admin":
            ## Kayıt formundaki alanları hazır getir
            data['isim'] = "musluyuksektepe"
            data['soyisim'] = "SONID: {}".format(sonID)
        else:
            data['isim'] = request.user

            data['coklusec'] = "1,3"
            data['sehir'] = "izmir"
            data['decimalfield'] = "10.12"
            data['soyisim'] = "SONID: {}".format(sonID)

        ## url ye parametre ekleyerek özel işlem yaptırmak
        ## Örn: http://0.0.0.0:8000/admin/kayitlar/kullanicilar/add/?toplamkayit
        toplamkayit = request.GET.get('toplamkayit', None)
        if toplamkayit != None:
            toplamkayit_sayisi = self.model.objects.count()

            print(toplamkayit_sayisi)

        ## Url parametre ile model adı gönderip son ID yi almak
        modeladi = request.GET.get('modeladi', None)
        if modeladi:
            ## Model adı KÜÇÜK yazılmalı
            ## Örn: http://0.0.0.0:8000/admin/kayitlar/kullanicilar/add/?modeladi=aylar
            ## ContentType modelinden istenilen modeli bul
            from django.contrib.contenttypes.models import ContentType
            ct = ContentType.objects.get(model=modeladi)
            ## Modeli class olarak al
            model = ct.model_class()
            ##İstenilen modele ait son ID yi bul
            istenilenmodel_son_id = model.objects.last().id
            print(istenilenmodel_son_id)
            ## Yeni kayıt sayfasında aylar alanını son id ye göre otomatik doldur
            data['aylar'] = istenilenmodel_son_id

        ## request içine oluşturulan data listesini ekle
        request.GET = data

        extra_context = extra_context or {}

        if str(request.user) != 'admin':
            ## Kullanıcı admin değilse Kaydet ve Düzenlemeye devam et butonunu gizleme
            extra_context['show_save_and_continue'] = False

        return super().add_view(request, form_url, extra_context)
