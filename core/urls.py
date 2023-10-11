from django.urls import path
from . import views
from .models import Profile
from .serializers import ProfileSerializer

urlpatterns = [
    path("profiles", views.ProfileList.as_view()),
    path("profiles/<int:pk>/", views.ProfileDetail.as_view()),
    path("users", views.UserList.as_view()),
    path("users/<int:pk>/", views.UserDetail.as_view()),
]
