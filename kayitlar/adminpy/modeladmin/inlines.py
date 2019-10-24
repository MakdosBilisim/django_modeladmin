from django.contrib import admin
from kayitlar.models import Kullanicilar, KullanicilaraAitInlineModel


class KullanicilaraAitInlineModelInline(admin.TabularInline): # Tablodaki alanları yan yana dizer.
# class KullanicilaraAitInlineModelInline(admin.StackedInline): # Tablodaki alanları alt alta sıralar
    model = KullanicilaraAitInlineModel
    max_num = 5                                 # En fazla girilecek kayıt sayısı
    min_num = 1                                 # En az kayıt sayısı
    extra = 1                                   # Inline ekleme linki tıklandıkça gösterilecek alan sayısı
    # raw_id_fields = []                        # Foreignkey ve ManyToManyField larda sadece id göster
    can_delete = True                           # Inlineda girilen kayıtların silinip/silinmeme yetkisi
    template = 'admin/edit_inline/tabular.html' # Özel html dosyası. NOT: admin.StackedInline yazılsa bile html yine tabular.html i gösterir.


@admin.register(Kullanicilar)
class KullanicilarAdmin(admin.ModelAdmin):
    list_display = ['isim', 'soyisim']
    inlines = [KullanicilaraAitInlineModelInline]
