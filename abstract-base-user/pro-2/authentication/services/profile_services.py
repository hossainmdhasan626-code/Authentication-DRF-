# ---Drf--
from rest_framework.exceptions import ValidationError

# ---Model---
from accounts.models import UserProfile

# ---Serializer---
from authentication.serializers import AuthenticationSerializer


class ProfileServices:
    # def get_profile(self, pk):
    def get_profile(self, data):

        # try:
        #     user_profile_query = UserProfile.objects.get(id=pk)
        # except UserProfile.DoesNotExist:
        #     raise ValidationError({"error": "User with this ID was not found."})

        serializer = AuthenticationSerializer(data)

        return serializer.data
