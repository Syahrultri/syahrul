
from django.contrib import admin
from django.urls import path
from django.http import HttpResponse
from django.shortcuts import render
from Dashboard.views import produk, tambah_barang, Barang_View

def coba1(request):
    return HttpResponse('Selamat Datang')

def coba2(request):
    titelnya="Home"
    konteks = {
        'titel':titelnya,
    }
    return render(request,'index.html',konteks)

urlpatterns = [
    path('admin/', admin.site.urls),
    path('',coba2),
    path('produk/',produk),
    path('addbrg/',tambah_barang),
    path('Vbrg/',Barang_View),
]
