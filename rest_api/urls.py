from django.urls import path
from rest_api.views.views_bus import BusListView, BusCreateView, BusUpdateView, BusDeleteView
from rest_api.views.views_bus_stop import BusStopListView, BusStopCreateView, BusStopUpdateView, BusStopDeleteView
from rest_api.views.views_driver import DriverListView, DriverCreateView, DriverUpdateView, DriverDeleteView
from rest_api.views.views_route import RouteListView, RouteCreateView, RouteUpdateView, RouteDeleteView

urlpatterns = [
    # Bus
    path('bus/view', BusListView.as_view(), name='bus_list'),
    path('bus/create', BusCreateView.as_view(), name='bus_create'),
    path('bus/update/<int:bus_id>', BusUpdateView.as_view(), name='bus_update'),
    path('bus/delete/<int:bus_id>', BusDeleteView.as_view(), name='bus_delete'),

    # Bus Stop
    path('bus_stop/view', BusStopListView.as_view(), name='bus_stop_list'),
    path('bus_stop/create', BusStopCreateView.as_view(), name='bus_stop_create'),
    path('bus_stop/update/<int:marker_id>', BusStopUpdateView.as_view(), name='bus_stop_update'),
    path('bus_stop/delete/<int:marker_id>', BusStopDeleteView.as_view(), name='bus_stop_delete'),

    # Driver
    path('driver/view', DriverListView.as_view(), name='driver_list'),
    path('driver/create', DriverCreateView.as_view(), name='driver_create'),
    path('driver/update/<int:driver_id>', DriverUpdateView.as_view(), name='driver_update'),
    path('driver/delete/<int:driver_id>', DriverDeleteView.as_view(), name='driver_delete'),

    # Route
    path('route/view', RouteListView.as_view(), name='route_list'),
    path('route/create', RouteCreateView.as_view(), name='route_create'),
    path('route/update/<int:route_id>', RouteUpdateView.as_view(), name='route_update'),
    path('route/delete/<int:route_id>', RouteDeleteView.as_view(), name='route_delete'),
]
