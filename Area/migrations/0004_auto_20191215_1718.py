# Generated by Django 2.2.6 on 2019-12-15 14:18

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('Area', '0003_auto_20191106_1743'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='info',
            name='info_img2',
        ),
        migrations.RemoveField(
            model_name='info',
            name='info_img3',
        ),
    ]
