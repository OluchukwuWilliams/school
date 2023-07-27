from django.db import models
# Create your models here.
from django.contrib.auth.models import User

# create your models here
class Category(models.Model):
    title = models.CharField(max_length=50)
    slug = models.SlugField()
    img = models.ImageField(upload_to='Category', default='category.jpg')
    description = models.TextField()

    def _str_(self):
        return self.title
    
class Contact(models.Model):
    STATUS_CHOICES = [
        ( 'New', 'New'),
        ('pending', 'pending'),
        ('completed', 'completed'),
    ]
    firstName = models.CharField(max_length=50)
    lastName = models.CharField(max_length=50)
    subject = models.CharField(max_length=70)
    email = models.EmailField()
    message = models.TextField()
    date_created = models.DateTimeField(auto_now_add=True)
    status = models.CharField(max_length=50, default='New', choices=STATUS_CHOICES)

    def __str__(self):
        return self.firstName
        
class Quiz(models.Model):
    category = models.ForeignKey(Category, on_delete=models.CASCADE)
    subject = models.CharField(max_length=50)
    slug = models.SlugField()
    date_updated = models.DateField(auto_now_add=True)

    def __str__(self):
        return self.title


