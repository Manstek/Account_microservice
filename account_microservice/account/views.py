from rest_framework import generics, viewsets, pagination, permissions, filters
from .serializers import (
    CustomUserSerializer, AccountSerializer, DoctorSerializer)
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


class CustomAccountViewSet(viewsets.ModelViewSet):
    permission_classes = [permissions.IsAuthenticated, IsAdmin]
    queryset = User.objects.all()
    serializer_class = AccountSerializer
    pagination_class = pagination.LimitOffsetPagination
    filter_backends = [filters.SearchFilter, ]


class DoctorViewSet(viewsets.ModelViewSet):
    queryset = User.objects.filter(role='doctor').all()
    serializer_class = DoctorSerializer
    http_method_names = ('get', 'list')
    filter_backends = [filters.SearchFilter, ]
    search_fields = ('full_name', )
