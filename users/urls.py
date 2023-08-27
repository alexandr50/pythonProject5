from django.contrib.auth.views import LoginView, LogoutView
from django.urls import path

from .apps import UsersConfig
from .views import confirm_code, UserProfileView, login_user

app_name = UsersConfig.name

urlpatterns = [
    #
    path('login/', login_user, name='login'),
    # path('login/', LoginView.as_view(template_name='users/login.html'), name='login'),
    path('confirm_code/<str:phone_number>/', confirm_code, name='confirm_code'),
    path('profile/<int:pk>/', UserProfileView.as_view(), name='profile'),
    path('logout/', LogoutView.as_view(), name='logout'),
]
