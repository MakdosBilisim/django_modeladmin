from django.http import HttpResponse
from django.shortcuts import render

from kayitlar.models import Kullanicilar


def ozelurl(request, yas=None, isim=None, soyisim=None):
    return HttpResponse("{} {} yas:{}".format(isim, soyisim, yas))


def anasayfa(request):
    kullanicilar = Kullanicilar.objects.all()
    d_ilebiten_kullanicilar = Kullanicilar.objects.filter(isim__endswith='da')

    kayitlar = [
        {'departman': 'IT', 'kullanici': {'adi': 'muslu', 'yas': 30}},
        {'departman': '<script>alert</script>', 'kullanici': {'adi': 'murat', 'yas': 25}},
    ]

    siralama = """
    muslu
    hasan
    murat"""

    htmlkod = '''
    <p>paragraf</p>
    <strong>strong</strong>
    <script>alert('alert');</script>
    '''

    icice_liste = ['Bir', ['Bir-1', ['Bir-1-1', 'Bir-1-2'], 'Bir-2']]

    return render(request, 'humanize/ordinal.html', {'kullanicilar': kullanicilar})

    # return render(request, 'humanize/naturaltime.html', {'kullanicilar': kullanicilar})
    # return render(request, 'humanize/naturalday.html', {'kullanicilar': kullanicilar})
    # return render(request, 'humanize/intword.html')
    # return render(request, 'humanize/intcomma.html')
    # return render(request, 'humanize/apnumber.html')
    # return render(request, 'yesno.html', {'kullanicilar': kullanicilar})
    # return render(request, 'wordwrap.html', {'kullanicilar': kullanicilar})
    # return render(request, 'wordcount.html', {'kullanicilar': kullanicilar})
    # return render(request, 'urlize.html', {'kayitlar': kayitlar})
    # return render(request, 'urlencode.html', {'kayitlar': kayitlar})
    # return render(request, 'unordered_list.html', {'icice_liste': icice_liste, 'kayitlar': kayitlar})
    # return render(request, 'truncatewords_html.html', {'htmlkod': htmlkod, 'siralama': siralama})
    # return render(request, 'truncatewords.html', {'htmlkod': htmlkod, 'siralama': siralama})
    # return render(request, 'truncatechars_html.html', {'htmlkod': htmlkod, 'siralama': siralama})
    # return render(request, 'truncatechars.html', {'kullanicilar': kullanicilar, 'siralama': siralama})
    # return render(request, 'title.html', {'kullanicilar': kullanicilar, 'siralama': siralama})
    # return render(request, 'timeuntil.html', {'kullanicilar': kullanicilar})
    # return render(request, 'timesince.html', {'kullanicilar': kullanicilar})
    # return render(request, 'time.html', {'kullanicilar': kullanicilar})
    # return render(request, 'striptags.html', {'kullanicilar': kullanicilar})
    # return render(request, 'stringformat.html', {'kullanicilar': kullanicilar})
    # return render(request, 'slugify.html', {'kullanicilar': kullanicilar})
    # return render(request, 'slice.html', {'kullanicilar': kullanicilar})
    # return render(request, 'safeseq.html', {'kullanicilar': kullanicilar })
    # return render(request, 'safe.html', {'htmlkod': htmlkod})
    # return render(request, 'random.html', {'kullanicilar': kullanicilar, 'kayitlar':kayitlar})
    # return render(request, 'pluralize.html', {'kullanicilar': kullanicilar})
    # return render(request, 'make_list.html', {'kullanicilar': kullanicilar})
    # return render(request, 'upper.html', {'kullanicilar': kullanicilar})
    # return render(request, 'lower.html', {'kullanicilar': kullanicilar})
    # return render(request, 'rjust.html', {'kullanicilar': kullanicilar})
    # return render(request, 'ljust.html', {'kullanicilar': kullanicilar})
    # return render(request, 'linenumbers.html', {'siralama': siralama})
    # return render(request, 'linebreaks.html', {'kullanicilar': kullanicilar})
    # return render(request, 'length_is.html', {'kullanicilar': kullanicilar})
    # return render(request, 'length.html', {'liste': [1, 2, 3], 'kayitlar': kayitlar, 'kullanicilar':kullanicilar, 'd_ilebiten_kullanicilar':d_ilebiten_kullanicilar})
    # return render(request, 'last.html', {'liste': [1, 2, 3, 4, 5], 'kayitlar': kayitlar})
    # return render(request, 'json_script.html', {'kayitlar': kayitlar})
    # return render(request, 'join.html', {'liste': [1, 2, 3, 'ab', 'ç']})
    # return render(request, 'get_digit.html', {'kullanicilar': kullanicilar})
    # return render(request, 'force_escape.html')
    # return render(request, 'floatformat.html')
    # return render(request, 'first.html', {'liste': [1, 2, 3, 4, 5], 'kullanicilar': kullanicilar})
    # return render(request, 'filesizeformat.html', {'kilobayt': 3535353535353 })
    # return render(request, 'escapejs.html', {'alert': 'alert("merhaba")'})
    # return render(request, 'divisibleby.html', {'kullanicilar': kullanicilar, 'bes':5})
    #
    # kayitlar = [
    #     {'departman': 'IT', 'kullanici': {'adi': 'muslu', 'yas': 30}},
    #     {'departman': 'IT', 'kullanici': {'adi': 'murat', 'yas': 25}},
    #     {'departman': 'IT', 'kullanici': {'adi': 'erdem', 'yas': 25}},
    #     {'departman': 'IT', 'kullanici': {'adi': 'dogancan', 'yas': 20}},
    # ]
    # return render(request, 'dictsortreversed.html', {'kullanicilar': kullanicilar, 'kayitlar': kayitlar})

    # return render(request, 'dictsort.html', {'kullanicilar': kullanicilar, 'kayitlar': kayitlar})
    # return render(request, 'default_if_none.html', {'kullanicilar': kullanicilar, 'd_ilebiten_kullanicilar': d_ilebiten_kullanicilar})
    # return render(request, 'default.html', {'kullanicilar': kullanicilar})
    # return render(request, 'date.html', {'kullanicilar': kullanicilar})
    # return render(request, 'cut.html', {'kullanicilar':kullanicilar})
    # return render(request, 'center.html', {'kullanicilar':kullanicilar})
    # return render(request, 'capfirst.html', {'kullanicilar':kullanicilar})
    # return render(request, 'addslashes.html')
    # return render(request, 'add.html', {
    #     'bes': 5,
    #     'liste': [1, 2, 3, 4, 5], 'digerliste': [6, 7, 8, 'string'],
    #     'stringdeger': 'isim',
    #     'kullanicilar': list(kullanicilar),
    #     'd_ilebiten_kullanicilar': list(d_ilebiten_kullanicilar)
    # })

    # return render(request, 'with.html', {'kullanicilar': kullanicilar})
    # return render(request, 'widthratio.html')
    # return render(request, 'url.html')
    # return render(request, 'verbatim.html')
    # return render(request, 'regroup.html', {'kullanicilar': kullanicilar})
    # return render(request, 'templatetag.html')
    # return render(request, 'spaceless.html')
    # return render(request, 'now.html')
    # return render(request, 'lorem.html')
    # return render(request, 'load.html')
    # return render(request, 'include.html', {'include_edilecek': 'include_edilecek.html'})

    # dict_deger = [
    #     {'isim': 'muslu', 'yas': 35},
    #     {'isim': 'murat', 'yas': 35},
    #     {'isim': 'erdem', 'yas': 35},
    #     {'isim': 'dogancan', 'yas': 26},
    #
    # ]
    #
    # return render(request, 'ifchanged.html', {
    #     'kullanici_listesi': kullanicilar,
    #     'dict_deger': dict_deger
    # })

    # ornek_dict = {1: 'elma', 2: 'armut'}
    # return render(request, 'if.html', {
    #     'kullanici_listesi': kullanicilar,
    #     'bos_kullanici_listesi': kullanicilar.filter(isim__endswith='yok'),
    #     'bes': 5,
    #     'ornek_dict': ornek_dict
    #
    # })

    # return render(request, 'for.html', {
    #     'kullanici_listesi': kullanicilar,
    #     'bos_kullanici_listesi': kullanicilar.filter(isim__endswith='yok'),
    #     'ornek_dict': ornek_dict,
    #
    # })

    # return render(request, 'firstof.html', {'bir': 1, 'iki': 2, 'uc': 3})
    # return render(request, 'filter.html')
    # return render(request, 'extends.html', {'extendadi': 'ozelklasor/base.html'})
    # return render(request, 'debug.html', {'kullanici_listesi': Kullanicilar.objects.all()})
    # return render(request, 'cycle.html')
    # return render(request, 'csrf_token.html')
    # return render(request, 'comment.html')
    # return render(request, 'block.html')
    # return render(request, 'autoescape.html', {'scriptalert': "<script>alert('Merrhaba')</script>"})
