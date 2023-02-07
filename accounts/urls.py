from django.urls import include  # , path
from django.urls import re_path as url
from rest_framework import routers

from .views import (
    UserViewSet,
    RegisterUserView
)

app_name = 'accounts'

router = routers.DefaultRouter()
router.register(r'users', UserViewSet, basename='user')
router.register(r'register', RegisterUserView, basename='register')

urlpatterns = [
    url(r'^', include(router.urls)),
]
