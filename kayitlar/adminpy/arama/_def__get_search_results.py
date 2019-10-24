from django.contrib import admin

from kayitlar.models import Kullanicilar


@admin.register(Kullanicilar)
class KullanicilarAdmin(admin.ModelAdmin):
    list_display = ['isim', 'soyisim', 'aylar']
    search_fields = ['soyisim']

    class Media:
        pass
        # js = ('',)
        # css = {'', }

    def get_search_results(self, request, queryset, search_term):
        queryset, use_distinct = super().get_search_results(request, queryset, search_term)

        print(queryset)
        print(search_term)
        print(request.user.username)

        aranan = search_term.strip()
        if not aranan:
            return queryset, use_distinct

        ## Sadece isim alanında ara
        # queryset = self.model.objects.filter(isim__startswith=aranan)

        ## search_fields de belirtilen alanlar ve isim alanında ara
        # queryset |= self.model.objects.filter(isim__contains=aranan)
        queryset |= self.model.objects.filter(isim__startswith=aranan)

        ## Kullanıcıya mesaj göstermek
        from django.contrib import messages

        ## Mesaj içeriğinde HTML etiketleri kullan
        from django.utils.safestring import mark_safe

        messages.warning(request, mark_safe('DİKKAT: Sadece isim alanında, aranan kelime ile başlayanlar sıralandı!. <b>(isim__startswith=aranan)</b>'))

        ## Kayıt sayısı
        print(queryset.count())
        ## Kayıt sayısı 1 den fazla ise uyarı göster
        if queryset.count() >= 1:
            messages.success(request, mark_safe('Aranan kelime <b style="color: orange;">TURUNCU</b> renk ile gösterildi.!'))

        self.Media.js = ('admin/mark/jquery.mark.min.js',) ## /home/.../modeladmin/static/admin/mark/jquery.mark.min.js
        self.Media.css = {'all': ('admin/mark/mark.css',)} ## /home/.../modeladmin/static/admin/mark/mark.css

        return queryset, use_distinct