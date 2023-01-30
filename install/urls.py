# from django.urls import include
from django.urls import re_path as url
# from rest_framework import routers
from install.views import installer

app_name = 'install'

# router = routers.DefaultRouter()
# router.register(r'install$', installer, basename='languages')

urlpatterns = [
    url(r'^$', installer),
]
