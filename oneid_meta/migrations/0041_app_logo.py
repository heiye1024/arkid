# Generated by Django 2.0.7 on 2019-07-17 04:03

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('oneid_meta', '0040_auto_20190716_1524'),
    ]

    operations = [
        migrations.AddField(
            model_name='app',
            name='logo',
            field=models.TextField(default='', verbose_name='LOGO'),
        ),
    ]
