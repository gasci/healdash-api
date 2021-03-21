from django.contrib import admin
from django.urls import path, include
from rest_framework.routers import DefaultRouter

from django.conf import settings
from django.conf.urls.static import static
from rest_framework_simplejwt.views import (
    TokenObtainPairView,
    TokenRefreshView,
)

from auth_app.views import MyObtainTokenPairView, RegisterView, TokenCheckView
from accounts.views import UserView, ListUsers

router = DefaultRouter()

urlpatterns = [
    path('admin/', admin.site.urls),
    path('login/', MyObtainTokenPairView.as_view(), name='token_obtain_pair'),
    path('login/refresh/', TokenRefreshView.as_view(), name='token_refresh'),
    path('register/', RegisterView.as_view(), name='auth_register'),
    path('token_check/', TokenCheckView.as_view(), name='token_check'),
    path('user/', ListUsers.as_view(), name='see_usernames'),
    path('', include(router.urls)),
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL,
                          document_root=settings.MEDIA_ROOT)
