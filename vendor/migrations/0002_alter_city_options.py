# Generated by Django 4.1 on 2022-09-16 19:11

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('vendor', '0001_initial'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='city',
            options={'ordering': ['name', 'country']},
        ),
    ]
