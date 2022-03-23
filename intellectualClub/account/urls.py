from unicodedata import name
from django.urls import path
from . import views
from django.contrib.auth import views as auth_views

urlpatterns = [
    path('edit_profile', views.UserEditView.as_view(), name='edit_profile'),
    path('regiter', views.RegisterUser.as_view(), name='register'),
    path('login', views.LoginUser.as_view(), name='login'),
    path('logout', views.logout_user, name='logout'),
    # path('password/', auth_views.PasswordChangeView.as_view(
    #     template_name='account/change-password.html'))

    path('password/', views.PasswordsChangeView.as_view(
        template_name='account/change-password.html')),
    path('password_success', views.password_success, name='password_success'),
]
