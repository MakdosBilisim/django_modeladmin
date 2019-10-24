from django.contrib import admin

from kayitlar.models import Kullanicilar


@admin.register(Kullanicilar)
class KullanicilarAdmin(admin.ModelAdmin):
    save_as = True  ## Kayıt düzenlenirken; kayıt aynen kalır yeni kayıt oluşturur. Kaydet ve başka birini ekle (Save and add another) yerine Yeni olarak kaydet (Save As New) olur. Güncelleme sonrası yeni ID ile yeni kayıt oluşur
    save_as_continue = False  ## True ve save_as = True ise kayıt düzenlerken Yeni olarak kaydet sonrası kayıt düzenleme sayfasına gelir. False olursa Kayıtların listesine döndürür.
