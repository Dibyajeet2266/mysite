# Generated by Django 2.1.5 on 2019-02-14 11:45

import datetime
from django.db import migrations, models
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0005_auto_20190214_1145'),
    ]

    operations = [
        migrations.AlterField(
            model_name='user',
            name='date_joined',
            field=models.DateTimeField(default=datetime.datetime(2019, 2, 14, 11, 45, 23, 592431, tzinfo=utc), verbose_name='date_joined'),
        ),
    ]
