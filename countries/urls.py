from django.urls import include  # , path
from django.urls import re_path as url
from rest_framework import routers
from countries.views import CountryAdminViewSet

app_name = 'countries'

router = routers.DefaultRouter()
router.register(r'countries', CountryAdminViewSet, basename='countries')

urlpatterns = [
    url(r'^', include(router.urls)),
]
