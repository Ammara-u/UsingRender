from django.db import models


class Sale(models.Model):
    sealName = models.CharField(max_length=200)  # Link to your inventory item
    quantity = models.IntegerField()
    sold_price = models.DecimalField(max_digits=10, decimal_places=2)
    date_sold = models.DateTimeField(auto_now_add=True)
    
# Create your models here.
class Seals(models.Model):
    nameOfSeal=models.CharField(max_length=200)
    partCode=models.IntegerField()
    description=models.CharField(max_length=300)
    price=models.IntegerField()
    stock=models.IntegerField(default=0)
    minStock = models.IntegerField(default=5)
 
# from django.utils import timezone
# Sale.objects.create(
#     seal_name="Seal A",
#     quantity=10,
#     total_price=500.0,
#     # date_sold=timezone.now()
# )