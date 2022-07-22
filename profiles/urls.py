from django.urls import include  # , path
from django.urls import re_path as url
from rest_framework import routers
from profiles.views import ProfileViewSet

app_name = 'profiles'

router = routers.DefaultRouter()
router.register(r'', ProfileViewSet, basename='profile')
urlpatterns = [
    url(r'', include(router.urls)),
]
