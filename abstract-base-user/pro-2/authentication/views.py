# ---Drf---
from rest_framework import status
from rest_framework.permissions import AllowAny, IsAuthenticated
from rest_framework.response import Response
from rest_framework.views import APIView

# ---Serializer---
from authentication.serializers import AuthenticationSerializer

# ---Services---
from authentication.services.profile_services import ProfileServices


# Create your views here.
class RegisterAPIView(APIView):
    permission_classes = [AllowAny]

    def post(self, request):

        password = request.data.get("password")
        refresh_password = request.data.get("confirm_password")

        if password == refresh_password:
            serializer = AuthenticationSerializer(data=request.data)
            serializer.is_valid(raise_exception=True)
            serializer.save()

            return Response(data=serializer.data, status=status.HTTP_201_CREATED)


class ProfileAPIView(APIView):
    permission_classes = [IsAuthenticated]

    # def get(self, request, pk):
    def get(self, request):

        data = ProfileServices().get_profile(data=request.user)

        return Response(data=data, status=status.HTTP_200_OK)
