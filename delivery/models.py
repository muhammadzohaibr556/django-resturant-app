from django.db import models
from resturant.models import Branches
from datetime import datetime
from django.urls import reverse
from django.utils.safestring import mark_safe
# Create your models here.

class Person(models.Model):
    name = models.CharField(max_length=200)
    phone = models.CharField(max_length=20)
    email = models.CharField(max_length=100)
    address = models.CharField(max_length=250, null=True)
    postal_code = models.CharField(max_length=20, null=True)
    created = models.DateTimeField(default=datetime.now())
    #paid = models.BooleanField(default=False)

    def __str__(self):
            return self.name

    def get_total_cost(self):
        return sum(item.get_cost() for item in self.items.all())

class Item(models.Model):
    title = models.CharField(max_length=200)
    photo = models.ImageField(upload_to='photos/%Y/%m/%d/', blank=True, null=True)
    price = models.PositiveIntegerField()
    category = models.CharField(max_length=20)

    def admin_photo_item(self):
        return mark_safe('<img src="{}" width="100" />'.format(self.photo.url))
    admin_photo_item.short_description = 'Item Image'
    admin_photo_item.allow_tags = True
   
    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return reverse('home')

class OrderItem(models.Model):
    order = models.ForeignKey(Person, on_delete=models.CASCADE)
    item = models.ForeignKey(Item, on_delete=models.DO_NOTHING)
    price = models.DecimalField(max_digits=10, decimal_places=2)
    quantity = models.PositiveIntegerField(default=1)
    from_branch = models.ForeignKey(Branches, on_delete=models.DO_NOTHING)
    paid = models.BooleanField(default=False)
    
    def __str__(self):
        return '{}'.format(self.id)

    def get_cost(self):
        return self.price * self.quantity


