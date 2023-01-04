from django.forms import ModelForm
from django import forms
from .models import *

class FormSebaran(ModelForm):
    class Meta:
        model = Ikan
        fields = '__all__'

        widgets = {
            'provinsi' : forms.TextInput({'class':'form-control', 'placeholder':'Provinsi', 'required':'required'}),
            'tahun18' : forms.NumberInput({'class':'form-control', 'placeholder':'Jumlah (Unit)'}),
            'tahun19' : forms.NumberInput({'class':'form-control', 'placeholder':'Jumlah (Unit)'}),
            'koordinat' : forms.TextInput({'class':'form-control', 'placeholder':'Koordinat', 'required':'required'}),
            'detail' : forms.TextInput({'class':'form-control', 'placeholder':'Detail', 'required':'required'}),    
            'usaha_id' : forms.Select({'class':'form-control', 'placeholder':'Jenis Usaha', 'required':'required'}),
        }


class FormBerita(ModelForm):
    class Meta:
        model = Berita
        fields = '__all__'

        widgets = {
            'judul' : forms.TextInput({'class':'form-control', 'placeholder':'Judul', 'required':'required'}),
            'img' : forms.FileInput({'class':'form-control', 'placeholder':'Gambar', 'required':'required'}),
            'publikasi' : forms.DateInput({'type':'date','class':'form-control', 'placeholder':'Publikasi', 'required':'required'}),
            'link' : forms.TextInput({'class':'form-control', 'placeholder':'Link', 'required':'required'}),
            'isi' : forms.TextInput({'class':'form-control', 'placeholder':'Isi', 'required':'required'}),    
            'jenis_id' : forms.Select({'class':'form-control', 'placeholder':'Jenis Berita', 'required':'required'}),
        }
