from rest_api.models import Inspector
from ..serializers import UserSerializer
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from rest_framework.permissions import IsAdminUser
from django.contrib.auth.models import User


class UserListView(APIView):
    permission_classes = [IsAdminUser]

    def get(self, request, *args, **kwargs):
        """
        List all registered users.
        """
        users = User.objects.all()
        serializer = UserSerializer(users, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)

    def post(self, request, *args, **kwargs):
        """
        Create a new user
        """
        serializer = UserSerializer(data=request.data)
        if serializer.is_valid(raise_exception=ValueError):
            user = serializer.create(validated_data=request.data)
            inspector = Inspector(user=user)
            inspector.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response({"error": True, "error_msg": serializer.error_messages}, status=status.HTTP_400_BAD_REQUEST)
