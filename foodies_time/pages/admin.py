from django.contrib import admin
from django.contrib.auth.models import User, Group 
from django.contrib.auth.admin import UserAdmin
from django.utils.translation import ugettext_lazy as _ 
# Register your models here.
class MyUserAdmin(UserAdmin): 

    list_display = ("username","first_name", "last_name", "email","is_active","is_staff")

    ## Static overriding 
    fieldsets = (
        (None, {'fields': ('username', 'password')}),
        (_('Personal info'), {'fields': ('first_name', 'last_name', 'email')}),
        (_('Permissions'), {'fields': ('is_active', 'is_staff', 'is_superuser')}),
        (_('Important dates'), {'fields': ('last_login', 'date_joined')}),
    )

# admin.site.unregister(User)
admin.site.unregister(Group)
#admin.site.register(User,MyUserAdmin)