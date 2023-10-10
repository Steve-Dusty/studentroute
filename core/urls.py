from django.urls import path
from . import views
from .models import Profile
from .serializers import ProfileSerializer

urlpatterns = [
    path("", views.ProfileList.as_view(queryset=Profile.objects.all(), serializer_class=ProfileSerializer))
]