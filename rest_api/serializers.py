from django.shortcuts import get_object_or_404
from rest_api.models import Bus, Driver, Route
from django.contrib.auth.models import User
from rest_framework import serializers


class UserSerializer(serializers.ModelSerializer):

    def create(self, validated_data):
        user = User.objects.create_user(**validated_data)
        return user

    class Meta:
        model = User
        fields = ('username', 'first_name', 'last_name', 'email', 'password')
        extra_kwargs = {
            'email': {'unique': True, 'required': True},
            'username': {'unique': True}
        }


# class BusSerializer(serializers.ModelSerializer):

#     def create(self, validated_data):
#         bus = Bus()
#         return user

#     class Meta:
#         model = Bus
#         fields = ('brand', 'plate', 'route')


class BusStopSerializer(serializers.ModelSerializer):

    def create(self, validated_data):
        user = User.objects.create_user(**validated_data)
        return user

    class Meta:
        model = User
        fields = ('username', 'first_name', 'last_name', 'email', 'password')
        extra_kwargs = {
            'email': {'unique': True, 'required': True},
            'username': {'unique': True}
        }


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
        fields = ('name', 'route_number')
