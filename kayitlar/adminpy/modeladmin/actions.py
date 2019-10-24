from django.contrib import admin

from kayitlar.models import Kullanicilar


@admin.register(Kullanicilar)
class KullanicilarAdmin(admin.ModelAdmin):

    # # Action
    def action_ornek(modeladmin, request, queryset):
        print("==============================action_ornek======================================")
        print(modeladmin)
        print(request.user)

        for kayit in queryset:
            print("==============================for kayit in queryset======================================")
            print(kayit.isim)
            kayit.soyisim = kayit.soyisim.lower()
            print("actions - Toplu olarak soyisimler küçük harfe çevrildi.")
            kayit.save()
            print("action dan kayıt edildi!")
            print("=+============================for kayit in queryset====================================+=")
        print("=+============================action_ornek====================================+=")
        return queryset

    actions = [action_ornek]
    actions_on_top = True  ## Sayfanın üst tarafında eylemler (actions) açılır kutusunu gösterir
    actions_on_bottom = True  ## Sayfanın altında eylemler açılır kutusunu gösterir
    actions_selection_counter = True  ## Eylem butonunun yanında seçili kayıt sayısını gösterir
