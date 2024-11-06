
from django.contrib import admin
from django.urls import path
from . import views
urlpatterns = [
    
    path('',views.home,name='home'),
    path('about/',views.about,name='about'),
    path('mbti/<int:pk>/', views.mbti_detail, name='mbti_detail'),  
]