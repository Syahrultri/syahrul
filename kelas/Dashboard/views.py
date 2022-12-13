from django.shortcuts import render
from Dashboard.forms import FormBarang
from Dashboard.models import Barang

# Create your views here.

def Barang_View(request):
    barangs=Barang.objects.all()

    konteks={
        'barangs':barangs,
    }
    return render(request,'tampil_brg.html',konteks)

def tambah_barang(request):
    titelnya="Barang"
    form=FormBarang()
    konteks={
        'form':form,
        'titel':titelnya,
    }
    return render(request,'tambah_barang.html',konteks)

def produk(request):
    titelnya="Produk"
    konteks = {
        'titel':titelnya,
    }
    return render(request,'produk.html',konteks)
