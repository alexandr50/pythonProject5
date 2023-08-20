from django.contrib.auth.views import LoginView
from django.urls import path

from .apps import UsersConfig
from .views import RegisterUserView, confirm_code

app_name = UsersConfig.name

urlpatterns = [

    path('register/', RegisterUserView.as_view(), name='register'),
    path('login/', LoginView.as_view(template_name='users/login.html'), name='login'),
    path('confirm_code/<str:phone_number>/', confirm_code, name='confirm_code')
]
