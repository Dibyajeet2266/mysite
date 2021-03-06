<<<<<<< HEAD
# Generated by Django 2.1.5 on 2019-02-14 11:44

import blog.models
import datetime
from django.db import migrations, models
import django.db.models.deletion
import django.utils.timezone
from django.utils.timezone import utc
=======
# Generated by Django 2.1.5 on 2019-02-13 12:22

import datetime
from django.conf import settings
import django.contrib.auth.models
from django.db import migrations, models
import django.db.models.deletion
import django.utils.timezone
>>>>>>> 426c05b0b589ccfac1b4a6cdfd835175e464f9bf


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('auth', '0009_alter_user_last_name_max_length'),
    ]

    operations = [
        migrations.CreateModel(
<<<<<<< HEAD
            name='User',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('password', models.CharField(max_length=128, verbose_name='password')),
                ('last_login', models.DateTimeField(blank=True, null=True, verbose_name='last login')),
                ('username', models.CharField(blank=True, max_length=256)),
                ('first_name', models.CharField(blank=True, max_length=256)),
                ('last_name', models.CharField(blank=True, max_length=256)),
                ('email', models.EmailField(blank=True, max_length=254, unique=True)),
                ('address1', models.CharField(blank=True, max_length=256)),
                ('address2', models.CharField(blank=True, max_length=256)),
                ('area_code', models.CharField(blank=True, max_length=10)),
                ('country_code', models.CharField(blank=True, max_length=10)),
                ('date_joined', models.DateTimeField(default=datetime.datetime(2019, 2, 14, 11, 44, 25, 308205, tzinfo=utc), verbose_name='date_joined')),
                ('is_active', models.BooleanField(default=True)),
                ('is_admin', models.BooleanField(default=False)),
                ('is_staff', models.BooleanField(default=False)),
                ('is_superuser', models.BooleanField(default=False)),
                ('groups', models.ManyToManyField(blank=True, help_text='The groups this user belongs to. A user will get all permissions granted to each of their groups.', related_name='user_set', related_query_name='user', to='auth.Group', verbose_name='groups')),
                ('user_permissions', models.ManyToManyField(blank=True, help_text='Specific permissions for this user.', related_name='user_set', related_query_name='user', to='auth.Permission', verbose_name='user permissions')),
            ],
            options={
                'verbose_name': 'user',
                'verbose_name_plural': 'users',
            },
            managers=[
                ('objects', blog.models.UserManager()),
            ],
        ),
        migrations.CreateModel(
=======
>>>>>>> 426c05b0b589ccfac1b4a6cdfd835175e464f9bf
            name='Comment',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('author', models.CharField(max_length=256)),
                ('text', models.TextField()),
                ('created_date', models.DateTimeField(default=django.utils.timezone.now)),
            ],
        ),
        migrations.CreateModel(
            name='Post',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=256)),
<<<<<<< HEAD
                ('start_date', models.DateField(default=datetime.date(2019, 2, 14))),
                ('end_date', models.DateField(default=datetime.date(2019, 2, 14))),
=======
                ('start_date', models.DateField(default=datetime.date(2019, 2, 13))),
                ('end_date', models.DateField(default=datetime.date(2019, 2, 13))),
>>>>>>> 426c05b0b589ccfac1b4a6cdfd835175e464f9bf
                ('amount_per_month', models.IntegerField(default=0)),
                ('amount_per_day', models.IntegerField(default=0)),
                ('start_date_pic', models.ImageField(blank=True, null=True, upload_to='')),
                ('end_date_pic', models.ImageField(blank=True, null=True, upload_to='')),
                ('rev1_status', models.IntegerField(default=0)),
                ('rev2_status', models.IntegerField(default=0)),
                ('rev3_status', models.IntegerField(default=0)),
                ('status', models.BooleanField(default=False)),
            ],
        ),
<<<<<<< HEAD
=======
        migrations.CreateModel(
            name='User',
            fields=[
                ('user_ptr', models.OneToOneField(auto_created=True, on_delete=django.db.models.deletion.CASCADE, parent_link=True, primary_key=True, serialize=False, to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'verbose_name': 'user',
                'verbose_name_plural': 'users',
                'abstract': False,
            },
            bases=('auth.user', models.Model),
            managers=[
                ('objects', django.contrib.auth.models.UserManager()),
            ],
        ),
>>>>>>> 426c05b0b589ccfac1b4a6cdfd835175e464f9bf
        migrations.AddField(
            model_name='comment',
            name='post',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='comments', to='blog.Post'),
        ),
    ]
