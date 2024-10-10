from django.urls import path, include
from djoser.views import UserViewSet

urlpatterns = [
    path('Authentication/SignUp/', UserViewSet.as_view({'post': 'create'})),
]
