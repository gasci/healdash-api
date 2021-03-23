from .views import EmployeesListView

from django.urls import path


urlpatterns = [
    path('list/', EmployeesListView.as_view(), name='list_employees'),
]
