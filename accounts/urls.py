from django.urls import include  # , path
from django.urls import re_path as url
from rest_framework import routers
from .views import (
    UserViewSet
)

app_name = 'accounts'

router = routers.DefaultRouter()
router.register(r'', UserViewSet, basename='account')
urlpatterns = [
    url(r'', include(router.urls)),
]
