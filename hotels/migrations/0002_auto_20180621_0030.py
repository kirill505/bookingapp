# Generated by Django 2.0.6 on 2018-06-20 16:30

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('hotels', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='hotel',
            name='city',
            field=models.CharField(choices=[('c01', 'Байкал'), ('c02', 'Аршан'), ('c03', 'Белокурихка')], default='c01', max_length=100),
        ),
        migrations.AlterField(
            model_name='hotel',
            name='location',
            field=models.CharField(choices=[('l01', 'Максимиха'), ('l02', 'Горячинск'), ('l03', 'Энхалук')], default='l01', max_length=100),
        ),
    ]