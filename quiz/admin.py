from django.contrib import admin
from quiz.models import Subject, Question, Choice, UserChoice

# # Register your models here.

admin.site.register(Subject)
admin.site.register(Question)
admin.site.register(Choice)
admin.site.register(UserChoice)