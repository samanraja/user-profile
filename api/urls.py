from django.conf.urls import url
from django.contrib import admin
from django.urls import path, include

from .views import UserCreateView, UserDeleteView, ProfileUpdateView, AddressCreateView, AddressUpdateView
from rest_framework.authtoken import views

urlpatterns = [
    path('login/', views.obtain_auth_token),
    path('create/', UserCreateView.as_view(), name='create_user'),
    path('delete/<int:pk>/', UserDeleteView.as_view(), name='delete_user'),
    url('profile/update/', ProfileUpdateView.as_view(), name='update_profile'),
    path('address/create/', AddressCreateView.as_view(), name='create_address'),
    path('address/update/<int:pk>/', AddressUpdateView.as_view(), name='update_address'),
]
