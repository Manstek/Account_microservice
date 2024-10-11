from rest_framework import generics
from .serializers import CustomUserRetrieveSerializer


class CustomUserView(generics.RetrieveAPIView):
    serializer_class = CustomUserRetrieveSerializer

    def get_object(self):
        return self.request.user
