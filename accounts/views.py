# views.py (if applicable)
from dj_rest_auth.registration.views import RegisterView
from .serializers import CustomRegisterSerializer
from rest_framework.permissions import AllowAny


class CustomRegisterView(RegisterView):
    serializer_class = CustomRegisterSerializer


from rest_framework import status
from rest_framework.response import Response
from rest_framework.views import APIView
from django.utils.translation import gettext_lazy as _
from django.contrib.auth import get_user_model
from accounts.serializers import CustomPasswordResetConfirmSerializer

User = get_user_model()

class CustomPasswordResetConfirmView(APIView):
    permission_classes = [AllowAny]

    def post(self, request):
        serializer = CustomPasswordResetConfirmSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response({"detail": _("Password has been reset successfully.")}, status=status.HTTP_200_OK)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
