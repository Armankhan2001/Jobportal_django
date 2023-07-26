# from django import admin
from django.urls import path
from account.views import UserPasswordResetView, SendPasswordResetEmailView,UserChangePasswordView,UserLoginView, UserProfileView,UserRegistrationView,PersonalInfo




urlpatterns = [
    path('register/', UserRegistrationView.as_view(),name='register'),
    path('login/', UserLoginView.as_view(),name='login'),
    path('profile/', UserProfileView.as_view(),name='profile'),
    path('changepassword/', UserChangePasswordView.as_view(),name='changepassword'),
    path('send-reset-password-email/', SendPasswordResetEmailView.as_view(),name='send-reset-password-email'),
    path('reset-password/<uid>/<token>/', UserPasswordResetView.as_view(),name='reset-password'),
    path('per/', PersonalInfo.as_view(),name='per'),


    
]