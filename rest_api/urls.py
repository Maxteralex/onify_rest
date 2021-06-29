from django.urls import path
from rest_api.views.views_user import UserListView

urlpatterns = [
    path('user/', UserListView.as_view(), name='users'),
]