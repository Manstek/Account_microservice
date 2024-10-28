from rest_framework import generics, viewsets, pagination, permissions, filters
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status
from rest_framework_simplejwt.tokens import AccessToken

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


@api_view(['POST'])
def introspect_token(request):
    token_str = request.data.get('token')
    if not token_str:
        return Response(
            {"detail": "Token is required."},
            status=status.HTTP_400_BAD_REQUEST)

    try:
        token = AccessToken(token_str)
        return Response({
            "active": True,
            "user_id": token['user_id'],
            "username": token['username'],
            "role": token.get('role', None)
        }, status=status.HTTP_200_OK)
    except Exception as e:
        return Response(
            {"active": False, "detail": str(e)},
            status=status.HTTP_401_UNAUTHORIZED)
