from django.contrib.auth import get_user_model
from rest_framework import status
from rest_framework.response import Response
from rest_framework.views import APIView
from .serializers import RegisterSerializer
from .permissions import IsAdminPermission

MyUser = get_user_model()


class RegistrationView(APIView):
    permission_classes = [IsAdminPermission, ]

    def post(self, request):
        data = request.data
        serializer = RegisterSerializer(data=data)
        if serializer.is_valid(raise_exception=True):
            serializer.save()
            return Response('Successfully registered', status=status.HTTP_201_CREATED)
