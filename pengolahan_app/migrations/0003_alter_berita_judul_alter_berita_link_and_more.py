# Generated by Django 4.1.2 on 2023-01-02 04:04

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('pengolahan_app', '0002_jenis_berita'),
    ]

    operations = [
        migrations.AlterField(
            model_name='berita',
            name='judul',
            field=models.CharField(max_length=100),
        ),
        migrations.AlterField(
            model_name='berita',
            name='link',
            field=models.CharField(max_length=100),
        ),
        migrations.AlterField(
            model_name='ikan',
            name='koordinat',
            field=models.IntegerField(null=True),
        ),
    ]