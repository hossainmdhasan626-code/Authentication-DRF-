# ---Django---
from django.urls import path

# ---Drf---
from rest_framework_simplejwt.views import (
    TokenObtainPairView,
    TokenRefreshView,
    TokenVerifyView,
)

# ---APIView---
from authentication.views import ProfileAPIView, RegisterAPIView

app_name = "authentication"

urlpatterns = [
    path("register/", RegisterAPIView.as_view(), name="register"),
    # path("profile/<int:pk/>/", ProfileAPIView.as_view(), name="profile"),
    path("profile/", ProfileAPIView.as_view(), name="profile"),
    path("token/", TokenObtainPairView.as_view(), name="token_obtain_pair"),
    path("token/refresh/", TokenRefreshView.as_view(), name="token_refresh"),
    path("token/verify/", TokenVerifyView.as_view(), name="token_verify"),
]
