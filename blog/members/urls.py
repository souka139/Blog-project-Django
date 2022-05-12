from re import template
from django import views
from django.urls import path
from .views import PasswordsChangeView, ShowProfilPageView, UserEditView, UserRegisterView,EditProfilPageView,CreateProfilePageView
from django.contrib.auth import views as auth_views
from . import views
urlpatterns = [
    path('register/',UserRegisterView.as_view(),name='register'),
    path('edit_profile/',UserEditView.as_view(),name='edit_profile'),
    # path('password/',auth_views.PasswordChangeView.as_view(template_name='registration/change-password.html')),
    path('password/',PasswordsChangeView.as_view(template_name='registration/change-password.html'),name='change_pass'),
    path('password_success/',views.password_success,name='password_success'),
    path('<int:pk>/profile',ShowProfilPageView.as_view(),name='show_profile_page'),
    path('<int:pk>/edit_profile_page',EditProfilPageView.as_view(),name='edit_profile_page'),
    path('create_profile_page',CreateProfilePageView.as_view(),name='create_profile_page'),
]
