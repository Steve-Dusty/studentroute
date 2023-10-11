from .models import Profile, Post, Pair
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import permissions, generics
from rest_framework.permissions import IsAdminUser
from .serializers import ProfileSerializer, UserSerializer
from django.contrib.auth import get_user_model

User = get_user_model()

class UserList(generics.ListCreateAPIView):
    queryset = User.objects.all()
    serializer_class = UserSerializer
    permission_classes = [IsAdminUser]

class UserDetail(generics.RetrieveAPIView):
    queryset = User.objects.all()
    serializer_class = UserSerializer

class ProfileList(generics.ListCreateAPIView):
    queryset = Profile.objects.all()
    serializer_class = ProfileSerializer
    permission_classes = [IsAdminUser]

    def list(self, request):
        # Note the use of `get_queryset()` instead of `self.queryset`
        queryset = self.get_queryset()
        serializer = ProfileSerializer(queryset, many=True)
        return Response(serializer.data)


class ProfileDetail(generics.RetrieveAPIView):
    queryset = Profile.objects.all()
    serializer_class = ProfileSerializer
