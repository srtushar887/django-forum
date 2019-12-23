from django.db import models
from django.contrib import messages, auth
from django.contrib.auth.models import User



class Profile(models.Model):
    user = models.ForeignKey(User,on_delete=models.CASCADE)
    image = models.ImageField(upload_to='photos/%y/%m/d',blank=True)

    def __str__(self):
        return self.user.username
