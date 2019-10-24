import sys

from django.contrib import admin
from django.shortcuts import render
from django.urls import path

from kayitlar.views import anasayfa, ozelurl

urlpatterns = [
    path('', anasayfa),

    path('ozel/<int:yas>/', ozelurl, name='ozel_url'),
    path('ozel/<str:isim>/<str:soyisim>/', ozelurl, name='ozel_url_muslu'),



    path('admin/', admin.site.urls),
]


def ozel_404(request, exception):
    return render(request, '404.html', {'exception': exception})


def ozel_500(request):
    type, value, tb = sys.exc_info()
    return render(request, '500.html', {'exception': value})


handler404 = ozel_404
handler500 = ozel_500
