# The code defines two Django models, `Sale` and `Seals`, for managing sales and inventory items
# respectively.
from django.db import models


class Sale(models.Model):
    # sealName = models.CharField(max_length=200)  # Link to your inventory item
    partCode = models.CharField(max_length=100, null=True, blank=True)
    quantity = models.IntegerField()
    sold_price = models.DecimalField(max_digits=10, decimal_places=2)
    date_sold = models.DateTimeField(auto_now_add=True)
    
# Create your models here.
class Seals(models.Model):
    # nameOfSeal=models.CharField(max_length=200)
    partCode = models.CharField(max_length=100, null=True, blank=True)
    description=models.CharField(max_length=300, blank=True,null=True,)
    price=models.IntegerField()
    stock=models.IntegerField(default=0)
    minStock = models.IntegerField(default=500)
 
# from django.utils import timezone
# Sale.objects.create(
#     seal_name="Seal A",
#     quantity=10,
#     total_price=500.0,
#     # date_sold=timezone.now()
# )