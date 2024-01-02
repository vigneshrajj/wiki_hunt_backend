from django.contrib import admin
from django.contrib.auth.admin import UserAdmin as BaseUserAdmin
from django.contrib.auth.models import User
from api.models import profile

class AdminProfileInline(admin.StackedInline):
    model = profile
    can_delete = False
    verbose_name_plural = 'profiles'

class ProfileUserAdmin(BaseUserAdmin):
    inlines = (AdminProfileInline,)

admin.site.unregister(User)
admin.site.register(User, ProfileUserAdmin)
