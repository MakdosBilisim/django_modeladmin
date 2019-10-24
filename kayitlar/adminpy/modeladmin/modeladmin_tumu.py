from django.contrib import admin

from kayitlar.models import Kullanicilar, Aylar


class KullanicilarAdmin(admin.ModelAdmin):

    def __init__(self, model, admin_site):
        ### __init__ bir kere çağrılır ve diğer alanları ezer
        print("__init__ çağrıldı")
        # self.list_display = [field.attname for field in Kullanicilar._meta.fields if field.attname != 'id']
        super().__init__(model, admin_site)

    list_display = ['isim', 'soyisim', 'islemtarih', 'islemtarih_saniye', 'id']
    # list_display = [field.attname for field in Kullanicilar._meta.fields]
    # list_display = [field.attname for field in Kullanicilar._meta.fields if field.attname != 'id']

    # list_display_links = list_display
    list_display_links = ['soyisim', 'id']
    # list_display_links = [field.attname for field in Kullanicilar._meta.fields]
    # list_display_links = [field.attname for field in Kullanicilar._meta.fields if field.attname != 'id'] # list_display de olmayan alanlar eklenemez. # Foreignkey ile kullanılamaz.

    # ordering = list_display
    # ordering = ['-isim']
    ordering = ['isim', '-soyisim']

    # list_filter = list_display
    list_filter = ['isim', 'soyisim']

    list_select_related = ('aylar',)  ## N+1 sorunu için tek seferde birleştirerek çağır. # () tuple kullanılacak ise tek eleman olamaz.

    list_per_page = 10  ## Sayfada gösterilecek kayıt sayısı
    list_max_show_all = 10  ## Tümünü seç te gösterilecek en fazla kayıt sayısı

    list_editable = ['isim']  ## list_display_links da olanlar kullanılamaz. Kaydet butonu her kaydı ayrı ayrı güncellemeye gönderir.
    search_fields = ['isim', 'soyisim']

    date_hierarchy = 'islemtarih'  # Tek seçim olduğu için string veya tuple olmalı

    save_on_top = True  ##Kayıt giriş veya düzenlemede kaydet butonları üstte de gösterilir
    save_as = True  ## Kayıt düzenlenirken; kayıt aynen kalır yeni kayıt oluşturur. Kaydet ve başka birini ekle (Save and add another) yerine Yeni olarak kaydet (Save As New) olur. Güncelleme sonrası yeni ID ile yeni kayıt oluşur
    save_as_continue = False  ## True ve save_as = True ise kayıt düzenlerken Yeni olarak kaydet sonrası kayıt düzenleme sayfasına gelir. False olursa Kayıtların listesine döndürür.

    preserve_filters = False  ## True iken Kayıt ekleme, düzenleme ve silme sonrası FİLTRE (arama değil) varsa aynen korur.

    ###################################################################################
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

    ###################################################################################

    def islemtarih_saniye(self, obj):
        return obj.islemtarih.strftime("%d %b %Y %H:%M:%S")

    islemtarih_saniye.admin_order_field = 'islemtarih'
    islemtarih_saniye.short_description = 'İşlem Zamanı'

    # inlines = []

    ###################################################################################
    # # Template
    ####### settings.TEMPLATES.APP_DIRS: True olmalı #########
    # add_form_template = None
    # change_form_template = None
    # change_list_template = None
    delete_confirmation_template = 'admin/kayitlar/kayit_sil.html'
    delete_selected_confirmation_template = 'admin/secili_kayitlari_sil.html'
    object_history_template = 'admin/gecmis_eylemler.html'
    # popup_response_template = None


###################################################################################

admin.site.register(Kullanicilar, KullanicilarAdmin)


class AylarAdmin(admin.ModelAdmin):
    list_display = ['ay_ismi']


admin.site.register(Aylar, AylarAdmin)
