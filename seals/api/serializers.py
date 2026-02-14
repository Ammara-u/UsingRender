from rest_framework.serializers import ModelSerializer
from ..models import Seals

class SealsSerializer(ModelSerializer):
    class Meta:
        model=Seals
        fields = ['id', 'partCode', 'description', 'price', 'stock', 'minStock']        

from rest_framework import serializers
from ..models import Sale

class SaleSerializer(serializers.ModelSerializer):
    total_price = serializers.SerializerMethodField()

    class Meta:
        model = Sale
        fields = ['id', 'partCode', 'quantity', 'sold_price', 'date_sold', 'total_price']

    def get_total_price(self, obj):
        return obj.quantity * obj.sold_price
