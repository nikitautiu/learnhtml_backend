# Generated by Django 2.0.6 on 2018-06-16 20:38

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('classification', '0004_auto_20180616_2038'),
    ]

    operations = [
        migrations.AlterField(
            model_name='pagedownload',
            name='date_downloaded',
            field=models.DateTimeField(auto_now=True, help_text='Date created', null=True),
        ),
    ]