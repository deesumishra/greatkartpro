from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from .models import Account
# Register your models here.
class AccountAdmin(UserAdmin):
    list_display = ('email','first_name','last_name','username','last_login','date_joined','is_active','is_staff','is_admin','is_superadmin')
    filter_horizontal=()
    list_filter = ()
    fieldsets = ()
admin.site.register(Account,AccountAdmin)