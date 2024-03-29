# Generated by Django 2.1.1 on 2019-01-23 11:31

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Aylar',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('ay_ismi', models.CharField(choices=[('Ocak', 'Ocak'), ('Şubat', 'Şubat'), ('Mart', 'Mart'), ('Nisan', 'Nisan'), ('Mayıs', 'Mayıs'), ('Haziran', 'Haziran'), ('Temmuz', 'Temmuz'), ('Ağustos', 'Ağustos'), ('Eylül', 'Eylül'), ('Ekim', 'Ekim'), ('Kasım', 'Kasım'), ('Aralık', 'Aralık')], max_length=15, verbose_name='Ay İsimleri')),
            ],
        ),
        migrations.CreateModel(
            name='CokluManytoMany',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('secimler', models.CharField(max_length=15, verbose_name='Çoklu Seçim')),
            ],
            options={
                'verbose_name': 'Seçim',
                'verbose_name_plural': 'Çoklu Seçim - M2M',
            },
        ),
        migrations.CreateModel(
            name='Kullanicilar',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('sehir', models.CharField(choices=[('adana', 'Adana'), ('izmir', 'İzmir'), ('istanbul', 'İstanbul')], default='adana', max_length=30, verbose_name='Şehir')),
                ('isim', models.CharField(help_text='Max: 30 karakter', max_length=30, verbose_name='İsim')),
                ('soyisim', models.CharField(help_text='Max: 60 karakter', max_length=60, verbose_name='Soyisim')),
                ('decimalfield', models.DecimalField(blank=True, decimal_places=2, max_digits=4, null=True)),
                ('islemtarih', models.DateTimeField(verbose_name='Tarih/Saat')),
                ('gorsel', models.ImageField(blank=True, null=True, upload_to='yuklenenler')),
                ('aylar', models.ForeignKey(blank=True, default=1, null=True, on_delete=django.db.models.deletion.CASCADE, to='kayitlar.Aylar', verbose_name='Aylar')),
                ('coklusec', models.ManyToManyField(to='kayitlar.CokluManytoMany', verbose_name='Çoklu Seçim M2M')),
                ('yazar', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL, verbose_name='Yazar')),
            ],
            options={
                'verbose_name': 'Kullanıcı',
                'verbose_name_plural': 'Kullanıcılar',
            },
        ),
        migrations.CreateModel(
            name='KullanicilaraAitInlineModel',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('charfield', models.CharField(default=None, max_length=80, verbose_name='Charfield')),
                ('integerfield', models.SmallIntegerField(default=0, verbose_name='SmalIntegerfield')),
                ('kullanicilar', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='kayitlar.Kullanicilar', verbose_name='Kullanıcılar')),
            ],
            options={
                'verbose_name': 'Inline',
                'verbose_name_plural': 'Örnek INline',
            },
        ),
    ]
