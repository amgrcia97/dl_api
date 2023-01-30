import debug_toolbar
from django.conf import settings
from django.conf.urls import include
from django.conf.urls.static import static
from django.contrib import admin
from django.urls import path, re_path as url

urlpatterns = [
    path('o/', include('oauth2_provider.urls', namespace='oauth2_provider')),
    url('^api-auth/', include('rest_framework.urls')),
    url('^accounts/', include('accounts.urls')),
    url('^languages/', include('languages.urls')),

    path('installer/', include('install.urls', namespace='take5_install')),
    url('^', admin.site.urls),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
urlpatterns = [
    path('__debug__/', include(debug_toolbar.urls)),
] + urlpatterns
