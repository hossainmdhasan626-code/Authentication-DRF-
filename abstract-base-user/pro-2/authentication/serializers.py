# ---Drf---
from rest_framework import serializers

# ---Model---
from accounts.models import UserProfile


class AuthenticationSerializer(serializers.ModelSerializer):
    class Meta:
        model = UserProfile
        fields = ["id", "name", "phone_number", "email", "password"]
        extra_kwargs = {"password": {"write_only": True}}

    def create(self, validated_data):

        user = UserProfile.objects.create_user(
            name=validated_data["name"],
            email=validated_data["email"],
            phone_number=validated_data["phone_number"],
            password=validated_data["password"],
        )

        return user
