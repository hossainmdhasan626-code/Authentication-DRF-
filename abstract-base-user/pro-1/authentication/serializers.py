# ---Drf---
from rest_framework import serializers

# ---Model---
from accounts.models import UserProfile


class SignupSerializer(serializers.ModelSerializer):
    class Meta:
        model = UserProfile
        fields = ["id", "username", "email", "password"]
        extra_kwargs = {"password": {"write_only": True}}

    def create(self, validated_data):

        user = UserProfile.objects.create_user(
            username=validated_data["username"],
            email=validated_data["email"],
            password=validated_data["password"],
        )

        return user
