from django.contrib import admin

from .models import Account
#from .forms import DietListForm, DietitianForm

# Register your models here.
@admin.register(Account)
class AccountAdmin(admin.ModelAdmin):
    list_display = ['user', 'is_active']
    search_fields = ['user__username']
    list_editable = ['is_active']
    ordering = ['-id']
    #form = DietitianForm
