from django.contrib import admin
from django.contrib.admin import ModelAdmin
from . models import *

# Register your models here.

class CategoryAdmin(admin.ModelAdmin):
    list_display = ['id', 'title', 'slug', 'img', 'description']
admin.site.register(Category, CategoryAdmin)

class QuizAdmin(admin.ModelAdmin):
    list_display = ['id', 'slug', 'date_updated', 'subject']
admin.site.register(Quiz, QuizAdmin)

class ContactAdmin(admin.ModelAdmin):
    list_display = ['id', 'firstName', 'lastName', 'subject', 'email', 'date_created', 'status']
admin.site.register(Contact, ContactAdmin)


