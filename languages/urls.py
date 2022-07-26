from django.urls import include  # , path
from django.urls import re_path as url
from rest_framework import routers
from languages.views import LanguageAdminViewSet, CountryLanguageViewSet

app_name = 'languages'

router = routers.DefaultRouter()
router.register(r'languages', LanguageAdminViewSet, basename='languages')
router.register(r'country_languages', CountryLanguageViewSet, basename='country_languages')

urlpatterns = [
    url(r'^', include(router.urls)),
]
