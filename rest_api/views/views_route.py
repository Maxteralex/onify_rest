from rest_api.models import Route
from ..serializers import RouteSerializer
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from django.shortcuts import get_object_or_404


class RouteListView(APIView):

    def get(self, request, *args, **kwargs):
        """
        List all stored routes.
        """
        routes = Route.objects.all()
        serializer = RouteSerializer(routes, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)


class RouteCreateView(APIView):

    def post(self, request, *args, **kwargs):
        """
        Create new route.
        """
        serializer = RouteSerializer(data=request.data)
        if serializer.is_valid(raise_exception=ValueError):
            route = serializer.create(validated_data=request.data)
            serializer.data['route_id'] = route.route_id
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response({"error": True, "error_msg": serializer.error_messages}, status=status.HTTP_400_BAD_REQUEST)


class RouteUpdateView(APIView):

    def post(self, request, route_id, *args, **kwargs):
        """
        Edit a stored route.
        """
        serializer = RouteSerializer(data=request.data)
        if serializer.is_valid(raise_exception=ValueError):
            serializer.update(validated_data=request.data, route_id=route_id)
            return Response(serializer.data, status=status.HTTP_200_OK)
        return Response({"error": True, "error_msg": serializer.error_messages}, status=status.HTTP_400_BAD_REQUEST)


class RouteDeleteView(APIView):

    def get(self, request, route_id, *args, **kwargs):
        """
        Remove a stored route.
        """
        route = get_object_or_404(Route, route_id=route_id)
        route.delete()
        return Response(status=status.HTTP_200_OK)
