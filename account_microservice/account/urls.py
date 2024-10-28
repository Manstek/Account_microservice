from django.urls import path, include

from djoser.views import UserViewSet

from rest_framework_simplejwt.views import (
    TokenObtainPairView, TokenRefreshView)
from rest_framework.routers import DefaultRouter

from .views import (
    RetrieveUserView, UpdateUserView, CustomAccountViewSet, DoctorViewSet)

router = DefaultRouter()
router.register(r'Accounts', CustomAccountViewSet)
router.register(r'Doctors', DoctorViewSet, basename='Doctors')

urlpatterns = [
    path('Authentication/SignUp/', UserViewSet.as_view({'post': 'create'})),
    path('Authentication/SignIn/', TokenObtainPairView.as_view()),
    path('Authentication/Refresh/', TokenRefreshView.as_view()),

    path('Accounts/Me/', RetrieveUserView.as_view()),
    path('Accounts/Update/', UpdateUserView.as_view()),
    path('', include(router.urls)),
]
