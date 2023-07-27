from django.urls import path
from . views import *
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('quiz/', views.quiz, name='quiz'),
    path('contact/', views.contact, name='contact'),
    # path('categories/<str:id>/', categories, name='categories'), 
    path('profile/', views.profile, name='profile'), 
    path('profile_update/', views.profile_update, name='profile_update'),  
    path('signin/', views.signin, name='signin'), 
    path('signout/', views.signout, name='signout'), 
    path('signup/', views.signup, name='signup'),
    path('password/', views.password, name='password'),
    path('economics/', views.economics, name='economics'),
    path('english/', views.english, name='english'),
    path('biology/', views.biology, name='biology'),
    path('mathematics/', views.mathematics, name='mathematics'),
    # path('addQuestion/', addQuestion, name='addQuestion'),
]