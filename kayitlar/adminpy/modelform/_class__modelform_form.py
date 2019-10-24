from django.contrib import admin
from django.forms import ModelForm, Textarea, NumberInput
from django.utils.safestring import mark_safe

from kayitlar.models import Kullanicilar

## Kayıt giriş ve düzenleme sırasında forma müdahale etmek
class KullanicilarForm(ModelForm):

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['isim'].strip = True
        self.fields['soyisim'].strip = True

    class Meta:
        model = Kullanicilar

        # fields = ['isim', 'aylar'] ## ModelAdmin deki fields değişkeni varsa burayı ezer.
        fields = '__all__'

        widgets = {
            'isim': Textarea(attrs={'cols': 20, 'rows': 0}),
            'decimalfield': NumberInput(attrs={'step': 0.25}),
        }
        labels = {
            'isim': 'form İsim_label',
            'soyisim': 'form Soyisim_label',
        }
        help_texts = {
            'isim': mark_safe('form İsim <b style="color:red;">help_texts</b>'),
            'soyisim': 'form Soyisim_help_texts',
        }
        error_messages = {
            'isim': {
                'required': mark_safe('Bu alan <b>zorunludur</b>!'),
            },
        }


@admin.register(Kullanicilar)
class KullanicilarAdmin(admin.ModelAdmin):
    list_display = ['isim', 'soyisim']
    fields = ['isim', 'soyisim', 'aylar', 'decimalfield']
    form = KullanicilarForm
