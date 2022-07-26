"""discere_linguis_api URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import include
from django.urls import re_path as url

urlpatterns = [
    # path('o/', include('oauth2_provider.urls', namespace='oauth2_provider')),
    url('^api-auth/', include('rest_framework.urls')),

    url('^accounts/', include('accounts.urls')),
    url('^countries/', include('countries.urls')),
    url('^genders/', include('genders.urls')),
    url('^languages/', include('languages.urls')),
    url('^professions/', include('professions.urls')),
    url('^profiles/', include('profiles.urls')),
    url('^', admin.site.urls),
]
