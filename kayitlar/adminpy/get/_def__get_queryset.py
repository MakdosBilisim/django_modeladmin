import inspect
from datetime import datetime, timedelta

from django.contrib import admin

from kayitlar.models import Kullanicilar


@admin.register(Kullanicilar)
class KullanicilarAdmin(admin.ModelAdmin):
    list_display = ['isim', 'soyisim', 'aylar', 'sehir', 'islemtarih', 'decimalfield']

    ## request e göre yetkilendirme.
    def get_queryset(self, request):
        print('------------>  Zaman: {}  .--> Def: {} <------------'.format(datetime.now(), inspect.stack()[0][3]))
        print('Çağıran: {}:{}, Fonksiyon:'.format(inspect.stack()[1][1], inspect.stack()[1][2]), inspect.stack()[1][3])

        print(request.user.username, request.user.is_superuser)

        if request.user.is_superuser:
            return self.model.objects.all()

        ## superuser olmayanlar sadece belirli kayıtları görsün
        # return self.model.objects.filter(isim__startswith='1').order_by('-sehir')

        if request.user.username == 'muslu':
            ## muslu kullanıcısı sadece dünki kayıtları görsün
            dun = (datetime.now() - timedelta(days=1)).day
            return self.model.objects.filter(islemtarih__day=dun)

        # sonUcgun = datetime.now() - timedelta(days=3)
        # return self.model.objects.filter(islemtarih__gte=sonUcgun)

        if request.user.username == 'serhat':
            ## muslu kullanıcısı decimalfield 0 ın altındakileri görsün
            return self.model.objects.filter(decimalfield__lte=0)

        ## Kayıt girenler sadece kendi kayıtlarını görsünler.
        # return self.model.objects.filter(yazar=request.user)

        # return self.model.objects.filter(decimalfield__gt=0)

        ## Kullanıcının dahil olduğu gruplar
        from django.contrib.auth.models import Group
        query_set = Group.objects.filter(user=request.user)

        for grup in query_set:
            grupadi = grup.name

            ## muhasebe grubundaki her kullanıcı
            if grupadi == 'muhasebe':

                ## muhasebe grubunda olan muslu kullanıcısı
                if request.user.username == 'muslu':
                    ## muslu kullanıcısı sadece dünki kayıtları görsün
                    dun = (datetime.now() - timedelta(days=1)).day
                    return self.model.objects.filter(islemtarih__day=dun)

                ## muhasebe grubundaki muslu harici diğer kullanıcılar
                return self.model.objects.filter(decimalfield=None, yazar=request.user)

            if grupadi == 'satis':
                return self.model.objects.filter(decimalfield__lte=0, yazar=request.user)

        ## Yazarlar sadece kendi kayıtlarını görebilir
        return self.model.objects.filter(yazar=request.user)
