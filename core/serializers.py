from rest_framework import serializers
from .models import Profile
from django.contrib.auth.models import User
from django.contrib.auth import get_user_model

User = get_user_model()

class ProfileSerializer(serializers.ModelSerializer):
    class Meta:
        model = Profile 
        fields = '__all__'

# serializes the raw abstract user
class UserSerializer(serializers.ModelSerializer):

    profile = ProfileSerializer()

    def create(self, validated_data):
        profile = validated_data.pop("profile")
        return User.objects.create(
            profile = Profile.objects.create(**profile),
            **validated_data,
        )


    class Meta:
        model = User
        fields = '__all__'
