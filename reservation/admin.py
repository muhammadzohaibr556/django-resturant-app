from django.contrib import admin
from .models import Reserve_Halls
#Register your models here.
class Reserve_HallsAdmin(admin.ModelAdmin):
    actions_selection_counter = False
    actions_on_bottom = False
    actions_on_top = False
    list_display = ['Name','Party_size', 'Date','Time','meal_type','hall','charges','paid']
    #list_filter = ['Name','Party_size', 'Date','Time','meal_type','hall','paid']
    list_editable = ['paid']

admin.site.register(Reserve_Halls,Reserve_HallsAdmin)
