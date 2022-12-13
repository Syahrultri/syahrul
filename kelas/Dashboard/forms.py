from socket import fromshare
from tkinter import Widget
from django.forms import ModelForm
from Dashboard.models import Barang
from django import forms

class FormBarang(ModelForm):
    class Meta :
        model=Barang
        fields='__all__'

        widget = {
            'kodebrg' : forms.TextInput({'class':'from-control'}),
            'nama' : forms.TextInput({'class':'from-control'}),
            'stok' : forms.NumberInput({'class':'from-control'}),
            'harga' : forms.NumberInput({'class':'from-control'}),
            'link_gbr' : forms.TextInput({'class':'from-control'}),
            'jenis_id' : forms.Select({'class':'from-control'}),
            
        }