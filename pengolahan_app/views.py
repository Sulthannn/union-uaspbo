from django.shortcuts import render, redirect
from .models import *
from .forms import *
from django.contrib import messages
from django.contrib.auth.decorators import login_required 
from django.conf import settings
from django.contrib.auth.forms import UserCreationForm
from django.db.models import Sum
# Create your views here.

def signup(request):
    if request.POST:
        form = UserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, "Admin Berhasil Dibuat!")
            return redirect('signup')
        else:
            messages.error(request, "Admin Gagal Dibuat!")
            return redirect('signup')
    else:
        form = UserCreationForm()
        data = {
            'form':form,
        }
    return render(request, 'signup.html', data)

def index(request):
    olah = Ikan.objects.all()
    data = {
        'Title' : "UNION || Sebaran",
        'olah' : olah,
    }
    return render(request, 'index.html', data)

@login_required(login_url=settings.LOGIN_URL)
def sebaran(request):
    olah = Ikan.objects.all()
    data = {
        'Title' : "UNION || Admin Sebaran",
        'olah' : olah,
    }
    return render(request, 'sebaran.html', data)

@login_required(login_url=settings.LOGIN_URL)
def tambahsebaran(request):
    if request.POST:
        form = FormSebaran(request.POST)
        if form.is_valid():
            form.save()
            form = FormSebaran()
            olah = Ikan.objects.all()
            pesan = "Data Sebaran Berhasil Ditambahkan!"
            data = {
            'Title' : "UNION || Tambah Sebaran",
            'olah' : olah,
            'form'  : form,
            'pesan' : pesan,
            }
            return render(request, 'tambahsebaran.html', data)
    else:
        form = FormSebaran()
        olah = Ikan.objects.all()
        data = {
           'Title' : "UNION || Tambah Sebaran",
           'olah' : olah,
           'form'  : form,
        }
    return render(request, 'tambahsebaran.html', data)

@login_required(login_url=settings.LOGIN_URL)
def updatesebaran(request, kl):
    ubaholah = Ikan.objects.get(pk=kl)
    if request.POST:
        form = FormSebaran(request.POST, instance=ubaholah)
        if form.is_valid():
            form.save()
            pesan = "Sebaran Berhasil Diupdate"
            data = {
                'Title' : "UNION || Ubah Sebaran",
                'ikan' : ubaholah,
                'form'  : form,
                'pesan' : pesan,
            }
            return render(request, 'updatesebaran.html', data)
    else:
        form = FormSebaran(instance=ubaholah)
        data = {
        'Title' : "UNION || Ubah Sebaran",
        'ikan' : ubaholah,
        'form'  : form,
         }
    return render(request, 'updatesebaran.html', data)

@login_required(login_url=settings.LOGIN_URL) 
def deletesebaran(request, kl):
    ikan = Ikan.objects.get(pk=kl)
    ikan.delete()
    
    return redirect("/sebaran/")


def info(request):
    total = Ikan.objects.aggregate(Sum('tahun18'))['tahun18__sum']
    total2 = Ikan.objects.aggregate(Sum('tahun19'))['tahun19__sum']
    artikel = Berita.objects.all()
    olah = Ikan.objects.all()
    data = {
        'Title' : "UNION || Beranda",
        'artikel' : artikel,
        'olah' : olah,
        'total' : total,
        'total2' : total2,
    }
    return render(request, 'info.html', data)

@login_required(login_url=settings.LOGIN_URL)
def berita(request):
    artikel = Berita.objects.all()
    data = {
        'Title' : "UNION || Admin Berita",
        'artikel' : artikel,
    }
    return render(request, 'berita.html', data)

@login_required(login_url=settings.LOGIN_URL)
def tambahberita(request):
    if request.POST:
        form = FormBerita(request.POST)
        if form.is_valid():
            form.save()
            form = FormBerita()
            artikel = Berita.objects.all()
            pesan = "Data Berita Berhasil Ditambahkan!"
            data = {
            'Title' : "UNION || Tambah Berita",
            'artikel' : artikel,
            'form'  : form,
            'pesan' : pesan,
            }
            return render(request, 'tambahberita.html', data)
    else:
        form = FormBerita()
        artikel = Berita.objects.all()
        data = {
           'Title' : "UNION || Tambah Berita",
           'artikel' : artikel,
           'form'  : form,
        }
    return render(request, 'tambahberita.html', data)

@login_required(login_url=settings.LOGIN_URL)
def updateberita(request, id):
    ubahberita = Berita.objects.get(pk=id)
    if request.POST:
        form = FormBerita(request.POST, instance=ubahberita)
        if form.is_valid():
            form.save()
            pesan = "Berita Berhasil Diupdate"
            data = {
                'Title' : "UNION || Ubah Berita",
                'berita' : ubahberita,
                'form'  : form,
                'pesan' : pesan,
            }
            return render(request, 'updateberita.html', data)
    else:
        form = FormBerita(instance=ubahberita)
        data = {
        'Title' : "UNION || Ubah Berita",
        'berita' : ubahberita,
        'form'  : form,
        }
    return render(request, 'updateberita.html', data)

@login_required(login_url=settings.LOGIN_URL) 
def deleteberita(request, id):
    berita = Berita.objects.get(pk=id)
    berita.delete()
    
    return redirect("/berita/")
