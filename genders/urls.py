from django.urls import include  # , path
from django.urls import re_path as url
from rest_framework import routers
from genders.views import GenderAdminViewSet

app_name = 'genders'

router = routers.DefaultRouter()
router.register(r'genders', GenderAdminViewSet, basename='languages')

urlpatterns = [
    url(r'^', include(router.urls)),
]
