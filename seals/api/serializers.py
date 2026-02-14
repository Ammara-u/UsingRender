from rest_framework.serializers import ModelSerializer
from ..models import Seals
class SealsSerializer(ModelSerializer):
    class Meta:
        model=Seals
        fields = ['id', 'partCode', 'description', 'price', 'stock', 'minStock']        
from rest_framework import serializers
from ..models import Seals, Sale

class SaleSerializer(serializers.ModelSerializer):
    # Change 'seal.nameOfSeal' to 'sealName' if that's your field name
    partCode = serializers.ReadOnlyField(source='partCode') 
    total_price = serializers.SerializerMethodField()

    class Meta:
        model = Sale
        # 2. Inclusion (This is where the fix happens)
        fields = [
            'id',  
            'partCode',  # <--- MUST be here!
            'quantity', 
            'sold_price', 
            'date_sold', 
            'total_price'
        ]
    def get_total_price(self, obj):
        return obj.quantity * obj.sold_price