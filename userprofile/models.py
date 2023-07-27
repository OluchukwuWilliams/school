from django.db import models
from django.contrib.auth.models import User 

# Create your models here.

class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    first_Name = models.CharField(max_length=100, default='ad')
    last_Name = models.CharField(max_length=100, default='ad')
    pix = models.ImageField(upload_to='Profile', default='avatar.png')
    email = models.EmailField()
    phone = models.CharField(max_length=50)
    gender = models.CharField(max_length=30)
    address = models.CharField(max_length=150)
    dob = models.CharField(max_length=20, default='a')
    nationality = models.CharField(max_length=30)
    state = models.CharField(max_length=50)

    def __str__(self):
        return self.user.username 