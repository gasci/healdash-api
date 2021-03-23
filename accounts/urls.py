from accounts.views import ListUsers

from django.urls import path


urlpatterns = [
    path('user/', ListUsers.as_view(), name='see_usernames'),
]
