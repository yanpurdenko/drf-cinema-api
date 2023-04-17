from rest_framework import generics
from rest_framework.permissions import IsAuthenticated
from rest_framework_simplejwt.authentication import JWTAuthentication

from user.serializers import UserSerializer


class CreateUserView(generics.CreateAPIView):
    """Endpoint for users register"""
    serializer_class = UserSerializer


class ManageUserView(generics.RetrieveUpdateAPIView):
    serializer_class = UserSerializer
    authentication_classes = (JWTAuthentication,)
    permission_classes = (IsAuthenticated,)

    def get_object(self):
        return self.request.user

    def get(self, request, *args, **kwargs):
        """Return a user as per id"""
        return super().retrieve(request, *args, **kwargs)

    def put(self, request, *args, **kwargs):
        """Update user as per id"""
        return super().update(request, *args, **kwargs)

    def patch(self, request, *args, **kwargs):
        """Partial update user as per id"""
        return super().partial_update(request, *args, **kwargs)
