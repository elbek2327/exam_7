from django.urls import path
from user import views
app_name = 'user'

urlpatterns = [
    path('', views.user_test, name='user_test'),
]