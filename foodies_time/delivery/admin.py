from django.contrib import admin
from .models import Item, Person, OrderItem
# Register your models here.
class PersonAdmin(admin.ModelAdmin):
    list_display = ['name','phone', 'email', 'address', 'postal_code']

class ItemAdmin(admin.ModelAdmin):
    actions_selection_counter = False
    actions_on_bottom = False
    actions_on_top = False
    list_display = ['admin_photo_item','title','price','category']
    #list_filter = ['category']
    #list_editable = ['price']

class OrderAdmin(admin.ModelAdmin):
    actions_selection_counter = False
    actions_on_bottom = False
    actions_on_top = False
    list_display = ['id', 'order', 'item', 'price', 'quantity', 'from_branch','paid']
    #list_filter = ['item', 'order', 'price', 'quantity','paid']
    list_editable = ['paid']

admin.site.register(Item, ItemAdmin)
#admin.site.register(Person, PersonAdmin)
admin.site.register(OrderItem, OrderAdmin)
