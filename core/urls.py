from django.urls import path
from . import views
from .models import *
from .serializers import *

urlpatterns = [
    path("profiles", views.ProfileList.as_view()),
    path("profiles/<int:pk>/", views.ProfileDetail.as_view()),
    path("users", views.UserList.as_view()),
    path("users/<int:pk>/", views.UserDetail.as_view()),
    path('login/', views.UserLoginView.as_view(), name='user-login'),
    path('dashboard/', views.PostList.as_view()),
    path('dashboard/<int:pk>/', views.PostDetail.as_view()),
    path('pair', views.PairList.as_view()),
    path('pair/<int:pk>', views.PairDetail.as_view())

]
