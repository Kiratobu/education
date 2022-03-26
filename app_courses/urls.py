from django.urls import path
from .import views

urlpatterns = [
    path('', views.courses_list, name='courses_list'),
    path('courses_info/', views.courses_info, name='courses_info'),
]
