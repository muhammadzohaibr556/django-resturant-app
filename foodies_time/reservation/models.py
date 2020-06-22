from django.db import models
from resturant.models import Halls, HallMeal
#  Create your models here.
class Reserve_Halls( models.Model):
    Name = models.CharField(max_length=100)
    Phone_no = models.CharField(max_length=20)
    Email = models.CharField(max_length=100)
    Party_size = models.CharField(max_length=50)
    Date = models.DateField()
    Time = models.CharField(max_length=100)
    meal_type = models.ForeignKey(HallMeal, on_delete=models.CASCADE)
    hall = models.ForeignKey(Halls, on_delete=models.CASCADE)
    charges = models.CharField(max_length=10, null=True)
    paid =  models.BooleanField(default=False)
    def __str__(self):
        return self.Name

    class Meta:
        db_table = "reserve_hall"
