from django.db import models
from django.db.models.fields.related import ForeignKey


class Bus(models.Model):
    bus_id = models.AutoField(primary_key=True)
    brand = models.CharField(max_length=128)
    plate = models.CharField(max_length=8)
    bus_number = models.IntegerField(blank=True, null=True)


class BusStop(models.Model):
    marker_id = models.AutoField(primary_key=True)
    latitude = models.FloatField()
    longitude = models.FloatField()
    title = models.CharField(max_length=128)
    address = models.TextField()


class Inspector(models.Model):
    inspector_id = models.AutoField(primary_key=True)
    user = ForeignKey('auth.User', on_delete=models.CASCADE)


class InspectorStop(models.Model):
    inspector_stop_id = models.AutoField(primary_key=True)
    inspector = ForeignKey('Inspector', on_delete=models.CASCADE)
    bus_stop = ForeignKey('BusStop', on_delete=models.CASCADE)


class Driver(models.Model):
    driver_id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=256)
    birth_date = models.DateTimeField()
    cpf = models.CharField(max_length=14)
    driver_license_type = models.CharField(max_length=1)
    civil_state = models.CharField(max_length=64)
    sex = models.CharField(max_length=1)


class RouteStop(models.Model):
    route_stop_id = models.AutoField(primary_key=True)
    route = models.ForeignKey('Route', on_delete=models.CASCADE)
    bus_stop = models.ForeignKey('BusStop', on_delete=models.CASCADE)


class Route(models.Model):
    route_id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=256)
    route_number = models.IntegerField()
