from rest_framework import serializers
from models import Profile
from django.contrib.auth.models import User


class ProfileSerializer(serializers.ModelSerializer):
    class Meta:
        model = User 
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
