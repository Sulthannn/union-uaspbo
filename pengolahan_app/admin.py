from django.contrib import admin

# Register your models here.
from .models import *

class olahadmin(admin.ModelAdmin):
    list_display = ['provinsi', 'tahun18', 'tahun19', 'koordinat', 'detail']
    search_fields = ['provinsi', 'koordinat']
    list_filter = ['usaha_id']
    list_per_page = 8

admin.site.register(Ikan, olahadmin)
admin.site.register(Usaha)

class beritaadmin(admin.ModelAdmin):
    list_display = ['judul', 'img', 'publikasi', 'link', 'isi']
    search_fields = ['judul', 'publikasi']
    list_filter = ['jenis_id']
    list_per_page = 8

admin.site.register(Berita, beritaadmin)
admin.site.register(Jenis)