from django.contrib import admin
from .models import customer
# Register your models here.

@admin.register(customer)
class CustomerAdmin(admin.ModelAdmin):
    list_display = ('id', 'name', 'email', 'password')