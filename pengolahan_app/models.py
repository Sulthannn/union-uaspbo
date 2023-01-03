from django.db import models

# Create your models here.

class Usaha(models.Model):
   nama = models.CharField(max_length=40)
   keterangan = models.TextField()

   def __str__(self):
      return self.nama

class Ikan(models.Model):
   provinsi = models.CharField(max_length=40)
   tahun18 = models.IntegerField(null=True)
   tahun19 = models.IntegerField(null=True)
   koordinat = models.CharField(max_length=100)
   detail = models.TextField()
   usaha_id = models.ForeignKey(Usaha, on_delete=models.CASCADE, null=True)
   
   def __str__(self):
      return self.provinsi



class Jenis(models.Model):
   nama = models.CharField(max_length=40)
   keterangan = models.TextField()

   def __str__(self):
      return self.nama

class Berita(models.Model):
   judul = models.CharField(max_length=100)
   img = models.CharField(null=True, max_length=40)
   publikasi = models.DateField(null=True)
   link = models.CharField(max_length=100)
   isi = models.TextField()
   jenis_id = models.ForeignKey(Jenis, on_delete=models.CASCADE, null=True)
   
   def __str__(self):
      return self.judul
