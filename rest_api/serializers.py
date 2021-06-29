from django.shortcuts import get_object_or_404
from rest_api.models import Bus, BusStop, Driver, Route
from rest_framework import serializers


class BusSerializer(serializers.ModelSerializer):

    def create(self, validated_data):
        bus = Bus(**validated_data)
        bus.save()
        return bus
    
    def update(self, validated_data, marker_id):
        bus = get_object_or_404(Bus, marker_id=marker_id)
        bus.brand = validated_data['brand']
        bus.plate = validated_data['plate']
        bus.bus_number = validated_data['bus_number']
        bus.save()
        return bus

    class Meta:
        model = Bus
        fields = ('brand', 'plate', 'bus_number')


class BusStopSerializer(serializers.ModelSerializer):

    def create(self, validated_data):
        bus_stop = BusStop(**validated_data)
        bus_stop.save()
        return bus_stop

    def update(self, validated_data, marker_id):
        bus_stop = get_object_or_404(BusStop, marker_id=marker_id)
        bus_stop.latitude = validated_data['latitude']
        bus_stop.longitude = validated_data['longitude']
        bus_stop.title = validated_data['title']
        bus_stop.address = validated_data['address']
        bus_stop.save()
        return bus_stop

    class Meta:
        model = BusStop
        fields = ('latitude', 'longitude', 'title', 'address')


class DriverSerializer(serializers.ModelSerializer):

    def create(self, validated_data):
        driver = Driver(**validated_data)
        driver.save()
        return driver
    
    def update(self, validated_data, driver_id):
        driver = get_object_or_404(Driver, driver_id=driver_id)
        driver.name = validated_data['name']
        driver.birth_date = validated_data['birth_date']
        driver.cpf = validated_data['birth_date']
        driver.driver_license_type = validated_data['birth_date']
        driver.civil_state = validated_data['birth_date']
        driver.sex = validated_data['birth_date']
        driver.save()
        return driver

    class Meta:
        model = Driver
        fields = ('name', 'birth_date', 'cpf', 'driver_license_type', 'civil_state', 'sex')


class RouteSerializer(serializers.ModelSerializer):

    def create(self, validated_data):
        route = Route(**validated_data)
        route.save()
        return route
    
    def update(self, validated_data, route_id):
        route = get_object_or_404(Route, route_id=route_id)
        route.name = validated_data['name']
        route.route_number = validated_data['route_number']
        route.save()
        return route

    class Meta:
        model = Route
        fields = ('route_id', 'name', 'route_number')
