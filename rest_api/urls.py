from django.urls import path
from rest_api.views import UserRecordView

urlpatterns = [
    path('user/', UserRecordView.as_view(), name='users'),
]