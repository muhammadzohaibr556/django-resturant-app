from django.contrib import admin
from .models import Branches, Halls, HallMeal
# Register your models here.
class BranchAdmin(admin.ModelAdmin):
    actions_selection_counter = False
    actions_on_bottom = False
    actions_on_top = False
    list_display = ['admin_photo_branch','name','address', 'phone']
    #list_filter = ['name']

class HallAdmin(admin.ModelAdmin):
    actions_selection_counter = False
    actions_on_bottom = False
    actions_on_top = False
    list_display = ['admin_photo_hall','title','size', 'capacity','charges_per_head']
    #list_filter = ['title', 'capacity', 'size']
    #list_editable = ['size', 'capacity','charges_per_head']

admin.site.register(Branches, BranchAdmin)
admin.site.register(Halls, HallAdmin)
admin.site.register(HallMeal)