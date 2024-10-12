from rest_framework import generics
from rest_framework import views
from .serializers import CustomUserSerializer, AccountSerializer
from .permissions import IsAdmin
from django.contrib.auth import get_user_model

User = get_user_model()


class RetrieveUserView(generics.RetrieveAPIView):
    serializer_class = CustomUserSerializer

    def get_object(self):
        return self.request.user


class UpdateUserView(generics.UpdateAPIView):
    serializer_class = CustomUserSerializer

    def get_object(self):
        return self.request.user


class CustomAccountView(views.APIView):
    permission_classes = [IsAdmin]
    queryset = User.objects.all()
    serializer_class = AccountSerializer
