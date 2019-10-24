from django.contrib import admin


from kayitlar.models import Kullanicilar


@admin.register(Kullanicilar)
class KullanicilarAdmin(admin.ModelAdmin):
    list_display = ['isim', 'soyisim', 'aylar', 'sehir', 'decimalfield']

    ## Kayıt silmeden önce kullanıcıya mesaj göstermek
    def get_deleted_objects(self, objs, request):
        for kayit in objs:

            if kayit.decimalfield and kayit.decimalfield >= 12:
                ## Kullanıcıya mesaj göstermek
                from django.contrib import messages

                ## Mesaj içeriğinde HTML etiketleri kullan
                from django.utils.safestring import mark_safe

                messages.warning(request, mark_safe('DİKKAT: Silinecek kayıt (<b>{} {}</b>) 12 dan büyük! -->{}'.format(kayit.isim, kayit.soyisim, kayit.decimalfield)))

        # print(request)

        from django.contrib.admin.utils import get_deleted_objects
        return get_deleted_objects(objs, request, self.admin_site)
