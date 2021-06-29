from rest_api.models import Driver
from ..serializers import DriverSerializer
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from rest_framework.permissions import IsAdminUser
from django.shortcuts import get_object_or_404


class DriverListView(APIView):

    def get(self, request, *args, **kwargs):
        """
        List all stored Drivers.
        """
        drivers = Driver.objects.all()
        serializer = DriverSerializer(drivers, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)


class DriverCreateView(APIView):

    def post(self, request, *args, **kwargs):
        """
        Create new Driver.
        """
        serializer = DriverSerializer(data=request.data)
        if serializer.is_valid(raise_exception=ValueError):
            serializer.create(validated_data=request.data)
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response({"error": True, "error_msg": serializer.error_messages}, status=status.HTTP_400_BAD_REQUEST)


class DriverUpdateView(APIView):

    def post(self, request, driver_id, *args, **kwargs):
        """
        Edit a stored Driver.
        """
        serializer = DriverSerializer(data=request.data)
        if serializer.is_valid(raise_exception=ValueError):
            serializer.update(validated_data=request.data, driver_id=driver_id)
            return Response(serializer.data, status=status.HTTP_200_OK)
        return Response({"error": True, "error_msg": serializer.error_messages}, status=status.HTTP_400_BAD_REQUEST)


class DriverDeleteView(APIView):

    def get(self, request, driver_id, *args, **kwargs):
        """
        Remove a stored Driver.
        """
        driver = get_object_or_404(Driver, driver_id=driver_id)
        driver.delete()
        return Response(status=status.HTTP_200_OK)
