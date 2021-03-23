from django.contrib import admin
from django.urls import path, include
from django.conf.urls import url
from django.conf import settings
from django.conf.urls.static import static

from rest_framework.routers import DefaultRouter
from accounts.views import UserView, ListUsers

router = DefaultRouter()

urlpatterns = [
    url(r'^admin/clearcache/', include('clearcache.urls')), # to clean cache
    path('admin/', admin.site.urls),
    path('auth/', include('auth_app.urls')),
    path('account/', include('accounts.urls')),
    path('', include(router.urls)),
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL,
                          document_root=settings.MEDIA_ROOT)
