from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from .models import User

class CustomUserAdmin(UserAdmin):
    model = User
    list_display = ['name', 'is_staff', 'is_active']
    search_fields = ['name']
    ordering = ['name']

    # If you want to customize the fieldsets for adding/editing users in admin
    fieldsets = UserAdmin.fieldsets + (
        # Custom fieldsets go here
    )
    add_fieldsets = UserAdmin.add_fieldsets + (
        # Custom add_fieldsets go here
    )

admin.site.register(User, CustomUserAdmin)