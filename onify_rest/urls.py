from django.contrib import admin
from django.urls import path, include
from rest_framework.authtoken import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('rest_api/', include('rest_api.urls')),
    path('rest_api_token_auth/', views.obtain_auth_token, name='rest_api_token_auth'),
]
