# Generated by Django 4.0.5 on 2022-07-07 21:55

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('phones', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='phone',
            name='image',
            field=models.CharField(max_length=128, verbose_name='Image'),
        ),
    ]
