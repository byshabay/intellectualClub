from unicodedata import name
from django.urls import path
from . import views

urlpatterns = [
    path('<int:pk>/edit_profile', views.UserEditView.as_view(), name='edit_profile'),
    path('regiter', views.RegisterUser.as_view(), name='register'),
    path('login', views.LoginUser.as_view(), name='login'),
    path('logout', views.logout_user, name='logout'),

    path('password/', views.PasswordsChangeView.as_view()),
    path('password_success', views.password_success, name='password_success'),
    path('<int:pk>/edit_profile_image', views.EditUserImage.as_view(),
         name='edit_profile_image'),
    path('<int:pk>/profile', views.ShowUserPageView.as_view(), name='profile'),
]
