from django.urls import path 
from quiz import views 

urlpatterns = [
    path('quiz/', views.quiz_home, name='quiz_home'),
    path('page/<int:subject_id>/', views.quiz_page, name='quiz_page'),
    path('page/<int:subject_id>/<int:page>/', views.quiz_page, name='quiz_page'),
    path('result/', views.quiz_result, name='quiz_result'),
    # path('profile/', profile, name='profile_update'),
    # path('profile_update/', profile_update, name='profile_update'),

]