from unicodedata import name
from django.urls import path, include, re_path
from rest_framework_simplejwt.views import (
    TokenObtainPairView,
    TokenRefreshView,
)

# from rest_framework.authtoken.views import obtain_auth_token
from . import views

urlpatterns = [
    path('auth/', include('djoser.urls')),
    path('token/', TokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),


    # path('auth/token', obtain_auth_token, name='token'),
    # path('<int:pk>/edit_profile', views.UserEditView.as_view(), name='edit_profile'),
    # path('regiter', views.RegisterUser.as_view(), name='register'),
    # path('login', views.LoginUser.as_view(), name='login'),
    # path('logout', views.logout_user, name='logout'),

    # path('password/', views.PasswordsChangeView.as_view()),
    # path('password_success', views.password_success, name='password_success'),
    path('<int:pk>/edit_profile_image', views.EditUserImage.as_view(),
         name='edit_profile_image'),
    path('<int:pk>/profile', views.ShowUserPageView.as_view(), name='show_profile'),
]
