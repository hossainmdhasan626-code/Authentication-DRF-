# ---Drf---
from rest_framework import status
from rest_framework.permissions import AllowAny
from rest_framework.response import Response
from rest_framework.views import APIView

# ---Serializer---
from authentication.serializers import SignupSerializer


# Create your views here.
class SignupAPIView(APIView):
    permission_classes = [AllowAny]

    def post(self, request):

        password = request.data.get("password", None)
        confirm_password = request.data.get("confirm_password", None)

        if password == confirm_password:
            serializer = SignupSerializer(data=request.data)
            serializer.is_valid(raise_exception=True)
            serializer.save()

            return Response(data=serializer.data, status=status.HTTP_201_CREATED)
