from django.db import models
from django.urls import reverse
from django.utils import timezone


# Create your models here.
class Post(models.Model):
    title  = models.CharField(max_length=256)
    start_date  = models.DateTimeField(default=timezone.now())
    end_date = models.DateTimeField(blank =True,null=True)
    amount_per_month = models.IntegerField(default=0)
    amount_per_day = models.IntegerField(default=0)
    start_date_pic = models.ImageField(blank=True,null=True)
    end_date_pic =   models.ImageField(blank=True,null=True)

    def get_absolute_url(self):
         return reverse('post_list')

    def __str__(self):
        return self.text
