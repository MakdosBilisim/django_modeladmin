# Generated by Django 2.1.1 on 2019-01-30 11:02

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('kayitlar', '0004_auto_20190125_1355'),
    ]

    operations = [
        migrations.AddField(
            model_name='kullanicilar',
            name='toplantitarih',
            field=models.DateTimeField(blank=True, null=True, verbose_name='Toplantı Tarihi'),
        ),
    ]
