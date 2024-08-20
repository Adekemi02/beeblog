from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from django.contrib.auth.models import User
from .models import ProfileModel


admin.site.register(ProfileModel)

# class CustomUserAdmin(UserAdmin):
#     fieldsets = (
#         (None, {'fields': ('username', 'password')}),
#         ('Personal info', {'fields': ('first_name', 'last_name', 'email')}),
#         ('Permissions', {'fields': ('is_active', 'is_staff', 'is_superuser', 'user_permissions')}),
#         ('Important dates', {'fields': ('last_login', 'date_joined')}),
#     )

#     add_fieldsets = (
#         (None, {
#             'classes': ('wide',),
#             'fields': ('username', 'email', 'password1', 'password2'),
#         }),
#     )

# admin.site.unregister(User)
# admin.site.register(User, CustomUserAdmin)
