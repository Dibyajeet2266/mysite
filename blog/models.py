from django.db import models
from django.urls import reverse
from django.utils import timezone
import datetime


# Create your models here.
class Post(models.Model):
    
    title  = models.CharField(max_length=256)
    start_date  = models.DateField(default = datetime.date.today())
    end_date = models.DateField(default = datetime.date.today())
    amount_per_month = models.IntegerField(default=0)
    amount_per_day = models.IntegerField(default=0)
    start_date_pic = models.ImageField(blank=True,null=True)
    end_date_pic =   models.ImageField(blank=True,null=True)
    rev1_status = models.IntegerField(default = 0)
    rev2_status = models.IntegerField(default = 0)
    rev3_status = models.IntegerField(default = 0)


    def get_absolute_url(self):
         return reverse('blog:post_detail')

    def __str__(self):
        return self.title

# class Comment(models.Model):
#     title = models.ForeignKey('')
