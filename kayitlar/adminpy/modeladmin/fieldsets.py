from django.contrib import admin

from kayitlar.models import Kullanicilar


@admin.register(Kullanicilar)
class KullanicilarAdmin(admin.ModelAdmin):
    ## fields den farkı, alanları ayrı ayrı fieldsetlerde gösterebilir.
    fieldsets = (
        (None, {  ## None alanın başlığı yok demek
            'fields': (('isim', 'soyisim'), 'sehir')  ## (isim, soyisim) yanyana alta sehir alanı
            # 'fields': (('isim', 'soyisim'), 'sehir')
        }),
        ('Dış Tablolar', {
            # 'classes': ('collapse',), ## Alanı gizle göster linki ekler
            'fields': ('aylar', 'coklusec'),
        }),
    )
