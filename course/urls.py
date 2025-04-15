from django.urls import path
from course import views

app_name = 'course'
urlpatterns = [
    path('home/', views.index, name='index'),
    path('', views.index, name='home'),
]