from django.urls import path, include
from djoser.views import UserViewSet
from rest_framework_simplejwt.views import (
    TokenObtainPairView, TokenRefreshView)
from .views import CustomUserView

urlpatterns = [
    path('Authentication/SignUp/', UserViewSet.as_view({'post': 'create'})),
    path('Authentication/SignIn/', TokenObtainPairView.as_view()),
    path('Authentication/Refresh/', TokenRefreshView.as_view()),

    # path('Accounts/Me/', UserViewSet.as_view({'get': 'retrieve'})),
    path('Accounts/Me/', CustomUserView.as_view()),
]
