from django.db import models
from django.utils.safestring import mark_safe
# Create your models here.
class Branches(models.Model):
    name = models.CharField(max_length=100)
    address = models.TextField()
    phone = models.CharField(max_length=20)    
    photo_branch = models.ImageField(upload_to='photos/%Y/%m/%d/')
    photo_1 = models.ImageField(upload_to='photos/%Y/%m/%d/', blank=True)
    photo_2 = models.ImageField(upload_to='photos/%Y/%m/%d/', blank=True)
    photo_3 = models.ImageField(upload_to='photos/%Y/%m/%d/', blank=True)
    photo_4 = models.ImageField(upload_to='photos/%Y/%m/%d/', blank=True)
    photo_5 = models.ImageField(upload_to='photos/%Y/%m/%d/', blank=True)
    photo_6 = models.ImageField(upload_to='photos/%Y/%m/%d/', blank=True)
    
    def admin_photo_branch(self):
        return mark_safe('<img src="{}" width="100" />'.format(self.photo_branch.url))
    admin_photo_branch.short_description = 'Branch Image'
    admin_photo_branch.allow_tags = True
    
    def __str__(self):
        return self.name

    class Meta: 
        db_table = "branches" # used to name tablep


class Halls( models.Model):
    branch_in = models.ForeignKey(Branches, on_delete=models.CASCADE)
    title = models.CharField(max_length=100)
    photo_hall = models.ImageField(upload_to='photos/%Y/%m/%d/')
    size = models.CharField(max_length=200)
    capacity = models.CharField(max_length=100)
    charges_per_head = models.CharField(max_length=10,default=None, null=True, blank=True)
    
    def admin_photo_hall(self):
        return mark_safe('<img src="{}" width="100" />'.format(self.photo_hall.url))
    admin_photo_hall.short_description = 'Hall Image'
    admin_photo_hall.allow_tags = True
    
    def __str__(self):
        return self.title

    class Meta:
        db_table = "halls"


class HallMeal( models.Model):
    meal_type = models.CharField(max_length=100)
    charges_per_head = models.CharField(max_length=10)
    def __str__(self):
        return self.meal_type

    class Meta:
        db_table = "hallmeal"
