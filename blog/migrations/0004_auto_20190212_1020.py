# Generated by Django 2.1.5 on 2019-02-12 10:20

import datetime
from django.db import migrations, models
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0003_auto_20190212_0517'),
    ]

    operations = [
        migrations.AlterField(
            model_name='post',
            name='end_date',
            field=models.DateField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='post',
            name='start_date',
            field=models.DateField(default=datetime.datetime(2019, 2, 12, 10, 20, 56, 459453, tzinfo=utc)),
        ),
    ]