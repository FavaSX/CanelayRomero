# Generated by Django 5.0.6 on 2024-06-22 18:01

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('reposteria', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='coctel',
            name='imagen',
            field=models.ImageField(null=True, upload_to='coctels'),
        ),
        migrations.AddField(
            model_name='pan_pascua',
            name='imagen',
            field=models.ImageField(null=True, upload_to='pan_pascuas'),
        ),
        migrations.AddField(
            model_name='torta',
            name='imagen',
            field=models.ImageField(null=True, upload_to='tortas'),
        ),
    ]
