# Generated by Django 2.2.6 on 2019-11-06 14:43

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Area', '0002_place_place_img'),
    ]

    operations = [
        migrations.AddField(
            model_name='info',
            name='info_img1',
            field=models.TextField(default='#', help_text='Ссылка на картинку', max_length=150),
        ),
        migrations.AddField(
            model_name='info',
            name='info_img2',
            field=models.TextField(default='#', help_text='Ссылка на картинку', max_length=150),
        ),
        migrations.AddField(
            model_name='info',
            name='info_img3',
            field=models.TextField(default='#', help_text='Ссылка на картинку', max_length=150),
        ),
    ]
