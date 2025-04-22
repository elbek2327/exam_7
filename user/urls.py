from django.urls import path
from user import views
from user.views import LoginView, LogoutView, RegisterView

app_name = 'user'

urlpatterns = [
    path('', views.user_test, name='user_test'),
    path('login/', LoginView.as_view(), name='login_page'),
    path('register/', RegisterView.as_view(), name='register_page'),
    path('log-out/', LogoutView.as_view(), name='logout_page'),
]