from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from .models import CustomUser

class CustomUserAdmin(UserAdmin):
    model = CustomUser
    fieldsets = UserAdmin.fieldsets + (
        (None, {'fields': ('full_name', 'mobile_number', 'citizenship_country', 'resident_country')}),
    )
    add_fieldsets = UserAdmin.add_fieldsets + (
        (None, {'fields': ('full_name', 'mobile_number', 'citizenship_country', 'resident_country')}),
    )

admin.site.register(CustomUser, CustomUserAdmin)
