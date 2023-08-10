from django.db import models
from django.contrib.auth.models import User

# from django.contrib.auth.models import User

# Create your models here.

class Subject(models.Model):
    name = models.CharField(max_length=255)

    def __str__(self):
        return self.name 
    
class Question(models.Model):
    subject = models.ForeignKey(Subject, on_delete=models.CASCADE)
    question_text = models.CharField(max_length=255)

    def __str__(self):
        return self.question_text 
    
    
class Choice(models.Model):
    question = models.ForeignKey(Question, on_delete=models.CASCADE)
    choice_text = models.CharField(max_length=255)
    is_correct = models.BooleanField(default=False)

class UserChoice(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    choice = models.ForeignKey(Choice, on_delete=models.CASCADE)