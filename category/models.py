from django.db import models
from datetime import datetime
from django.contrib.auth.models import User
# Create your models here.
class Category(models.Model):
    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name

class Post(models.Model):
    category = models.ForeignKey(Category,on_delete=models.CASCADE,default=1,blank=True)
    user = models.ForeignKey(User,on_delete=models.CASCADE,default=1,blank=True)
    title = models.TextField(blank=True)
    des = models.TextField(blank=True)
    posted_date = models.DateTimeField(default=datetime.now,blank=True)

    def __str__(self):
        return self.title

