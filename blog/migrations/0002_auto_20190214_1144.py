# Generated by Django 2.1.5 on 2019-02-14 11:44

import datetime
from django.db import migrations, models
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='user',
            name='date_joined',
            field=models.DateTimeField(default=datetime.datetime(2019, 2, 14, 11, 44, 36, 674531, tzinfo=utc), verbose_name='date_joined'),
        ),
    ]
