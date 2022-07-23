from django.urls import include  # , path
from django.urls import re_path as url
from rest_framework import routers
from professions.views import ProfessionAdminViewSet

app_name = 'professions'

router = routers.DefaultRouter()
router.register(r'professions', ProfessionAdminViewSet, basename='professions')

urlpatterns = [
    url(r'^', include(router.urls)),
]
