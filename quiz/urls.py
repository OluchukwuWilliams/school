from django.urls import path 
from quiz import views 
from .views import quiz_result

urlpatterns = [
    path('quiz/', views.quiz_home, name='quiz_home'),
    path('page/<int:subject_id>/', views.quiz_page, name='quiz_page'),
    path('page/<int:subject_id>/<int:page>/', views.quiz_page, name='quiz_page'),
    path('result/<int:score>/', views.quiz_result, name='result'),
    path('calculate_score/', views.calculate_score, name='calculate_score'),

]