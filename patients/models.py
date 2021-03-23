from django.db import models
from django.utils import timezone

# Create your models here.


class Patient(models.Model):
    first_name = models.CharField(max_length=100, default="")
    last_name = models.CharField(max_length=100, default="")
    id_number = models.CharField(max_length=100, blank=True)
    role = models.CharField(max_length=100, default="", blank=True)
    country_code = models.CharField(max_length=30, default="", blank=True)
    telephone = models.CharField(max_length=100, default="", blank=True)
    start_date = models.DateTimeField(default=timezone.now)
    leave_date = models.DateTimeField(blank=True, null=True)
    cost = models.CharField(max_length=100, default="", blank=True)
    profit = models.CharField(max_length=100, default="", blank=True)
    address = models.CharField(max_length=1000, default="", blank=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.first_name + " " + self.last_name
