from rest_api.models import Bus
from ..serializers import BusSerializer
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from rest_framework.permissions import IsAdminUser
from django.shortcuts import get_object_or_404


class BusListView(APIView):

    def get(self, request, *args, **kwargs):
        """
        List all stored Buses.
        """
        buses = Bus.objects.all()
        serializer = BusSerializer(buses, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)


class BusCreateView(APIView):

    def post(self, request, *args, **kwargs):
        """
        Create new Bus.
        """
        serializer = BusSerializer(data=request.data)
        if serializer.is_valid(raise_exception=ValueError):
            bus = serializer.create(validated_data=request.data)
            serializer.data['bus_id'] = bus.bus_id
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response({"error": True, "error_msg": serializer.error_messages}, status=status.HTTP_400_BAD_REQUEST)


class BusUpdateView(APIView):

    def post(self, request, bus_id, *args, **kwargs):
        """
        Edit a stored Bus.
        """
        serializer = BusSerializer(data=request.data)
        if serializer.is_valid(raise_exception=ValueError):
            serializer.update(validated_data=request.data, bus_id=bus_id)
            return Response(serializer.data, status=status.HTTP_200_OK)
        return Response({"error": True, "error_msg": serializer.error_messages}, status=status.HTTP_400_BAD_REQUEST)


class BusDeleteView(APIView):

    def get(self, request, bus_id, *args, **kwargs):
        """
        Remove a stored Bus.
        """
        bus = get_object_or_404(Bus, bus_id=bus_id)
        bus.delete()
        return Response(status=status.HTTP_200_OK)
