from django.urls import include
from django.urls import re_path as url
from rest_framework import routers
from languages.views import LanguageAdminViewSet

app_name = 'languages'

router = routers.DefaultRouter()
router.register(r'languages', LanguageAdminViewSet, basename='languages')

urlpatterns = [
    url(r'^', include(router.urls)),
]
