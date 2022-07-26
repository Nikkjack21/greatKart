from django.contrib import admin
from .models import Account
from django.contrib.auth.admin import UserAdmin
# Register your models here.

class AccountAdmin(UserAdmin):
    list_display = ('username', 'first_name', 'last_name', 'email', 'last_login','date_joined', 'is_active' )

    filter_horizontal = ()
    list_filter = ()
    fieldsets = ()



admin.site.register(Account, AccountAdmin)