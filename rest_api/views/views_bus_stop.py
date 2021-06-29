from rest_api.models import BusStop
from ..serializers import BusStopSerializer
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from rest_framework.permissions import IsAdminUser
from django.shortcuts import get_object_or_404


class BusStopListView(APIView):
    permission_classes = [IsAdminUser]

    def get(self, request, *args, **kwargs):
        """
        List all stored Bus Stops.
        """
        bus_stops = BusStop.objects.all()
        serializer = BusStopSerializer(bus_stops, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)


class BusStopCreateView(APIView):
    permission_classes = [IsAdminUser]

    def post(self, request, *args, **kwargs):
        """
        Create new Bus Stop.
        """
        serializer = BusStopSerializer(data=request.data)
        if serializer.is_valid(raise_exception=ValueError):
            serializer.create(validated_data=request.data)
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response({"error": True, "error_msg": serializer.error_messages}, status=status.HTTP_400_BAD_REQUEST)


class BusStopUpdateView(APIView):
    permission_classes = [IsAdminUser]

    def post(self, request, bus_stop_id, *args, **kwargs):
        """
        Edit a stored Bus Stop.
        """
        serializer = BusStopSerializer(data=request.data)
        if serializer.is_valid(raise_exception=ValueError):
            serializer.update(validated_data=request.data, bus_stop_id=bus_stop_id)
            return Response(serializer.data, status=status.HTTP_202_ACCEPTED)
        return Response({"error": True, "error_msg": serializer.error_messages}, status=status.HTTP_400_BAD_REQUEST)


class BusStopDeleteView(APIView):
    permission_classes = [IsAdminUser]

    def get(self, request, bus_stop_id, *args, **kwargs):
        """
        Remove a stored Bus Stop.
        """
        bus_stop = get_object_or_404(BusStop, bus_stop_id=bus_stop_id)
        bus_stop.delete()
        return Response(status=status.HTTP_200_OK)
