import inspect
from datetime import datetime

from django import forms
from django.contrib import admin

from kayitlar.models import Kullanicilar, Aylar


class FielLabelDegistir(forms.ModelChoiceField):
    def label_from_instance(self, obj):

        ## Ay ismini numaraya çevir
        from time import strptime
        ay_sirasi = strptime(obj.ay_ismi, '%B').tm_mon

        ## Ay numarasına göre mevsim bul
        if ay_sirasi in (12, 1, 2): mevsim = 'Kış'
        if ay_sirasi in (3, 4, 5): mevsim = 'İlkbahar'
        if ay_sirasi in (6, 7, 8): mevsim = 'Yaz'
        if ay_sirasi in (9, 10, 11): mevsim = 'Sonbahar'

        ## Açılır kutuda mevsim ve alanın değerini yaz
        return "{}: {}".format(mevsim, obj.ay_ismi)


@admin.register(Kullanicilar)
class KullanicilarAdmin(admin.ModelAdmin):
    list_display = ['isim', 'soyisim', 'aylar']

    def formfield_for_foreignkey(self, db_field, request=None, **kwargs):
        print('------------>  Zaman: {}  .--> Def: {} <------------'.format(datetime.now(), inspect.stack()[0][3]))
        print('Çağıran: {}:{}, Fonksiyon:'.format(inspect.stack()[1][1], inspect.stack()[1][2]), inspect.stack()[1][3])

        if db_field.name == 'aylar':
            ## Alan adı aylar ise Label değiştirme fonksiyonunu çağır
            return FielLabelDegistir(queryset=Aylar.objects.all())

        return super().formfield_for_foreignkey(db_field, request, **kwargs)
