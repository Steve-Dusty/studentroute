from .models import Profile, Post
from rest_framework import status
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.authtoken.models import Token
from rest_framework import permissions, generics
from rest_framework.permissions import IsAdminUser, AllowAny, IsAuthenticated
from .serializers import *
from django.contrib.auth import get_user_model, authenticate, login
 
User = get_user_model()
 
# any class ending with "List" is going to be a signup functionality
class UserList(generics.ListCreateAPIView):
    queryset = User.objects.all()
    serializer_class = UserSerializer
    # permission_classes = [IsAdminUser]
 
class UserDetail(generics.RetrieveAPIView):
    queryset = User.objects.all()
    serializer_class = UserSerializer
 
class ProfileList(generics.ListCreateAPIView):
    queryset = Profile.objects.all()
    serializer_class = ProfileSerializer
    #permission_classes = [IsAdminUser]
 
    def list(self, request):
        # Note the use of `get_queryset()` instead of `self.queryset`
        queryset = self.get_queryset()
        serializer = ProfileSerializer(queryset, many=True)
        return Response(serializer.data)
 
class ProfileDetail(generics.RetrieveAPIView):
    queryset = Profile.objects.all()
    serializer_class = ProfileSerializer
 
# login
class UserLoginView(APIView):
    permission_classes = [AllowAny]
 
    def post(self, request):
        serializer = UserLoginSerializer(data=request.data)
        if serializer.is_valid():
            email = serializer.validated_data['email']
            password = serializer.validated_data['password']
            user = authenticate(email=email, password=password)
 
            if user is not None:
                # token based login
                token, _ = Token.objects.get_or_create(user=user)
                return Response({'token': token.key})
            else:
                return Response({'error': 'Invalid credentials'}, status=status.HTTP_401_UNAUTHORIZED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
 
class PostList(generics.ListCreateAPIView):
    queryset = Post.objects.all()
    serializer_class = PostSerializer
 
    def create(self, request, *args, **kwargs):
        existing_post = Post.objects.filter(rider=request.data['rider'])
        if existing_post:
            existing_post.delete()
 
 
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        self.perform_create(serializer)
        return Response(serializer.data, status=status.HTTP_201_CREATED)
 
class PostDetail(generics.RetrieveAPIView):
    queryset = Post.objects.all()
    serializer_class = PostSerializer
 
 
class DriverList(generics.ListCreateAPIView):
    queryset = Driver.objects.all()
    serializer_class = DriverSerializer
 
 
class DriverDetail(generics.RetrieveAPIView):
    queryset = Driver.objects.all()
    serializer_class = DriverSerializer
 
class RiderList(generics.ListCreateAPIView):
    queryset = Rider.objects.all()
    serializer_class = RiderSerializer
 
class RiderDetail(generics.RetrieveUpdateAPIView):
    queryset = Rider.objects.all()
    serializer_class = RiderSerializer
 
    def perform_update(self, serializer):
        rider_instance = self.get_object()
        associated_post = Post.objects.get(rider=rider_instance)
        if associated_post:
            associated_post.delete()
 
 
