from django.db import models
from django.utils import timezone

# Create your models here.
cate = (('Music','Music'),('Book','Book'),('Movie','Movie'),('Morter','Morter'),('Others',"Others"))
class Subsc(models.Model):
    title = models.CharField(max_length=100)
    url = models.URLField(max_length=200)    
    price = models.PositiveSmallIntegerField(default=0)
    date = models.DateField(default=timezone.now)
    period = models.IntegerField(default = 0)
    category = models.CharField(max_length=100,choices = cate,default=('Music'))
    dateleft = models.IntegerField(default=0)



    def __str__(self):
        return self.title






