from .views import RegisterUserAPI, RegisterClientAPI
from django.urls import path

urlpatterns = [
    path('register_user/', RegisterUserAPI.as_view(), name='register_user'),
    path('register_client/', RegisterClientAPI.as_view(), name='register_client'),
]