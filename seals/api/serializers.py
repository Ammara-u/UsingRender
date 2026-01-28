from rest_framework.serializers import ModelSerializer
from ..models import Seals
class SealsSerializer(ModelSerializer):
    class Meta:
        model=Seals
        fields = ['id', 'nameOfSeal', 'partCode', 'description', 'price', 'stock']        
from rest_framework import serializers
from ..models import Seals, Sale

class SaleSerializer(serializers.ModelSerializer):
    # Change 'seal.nameOfSeal' to 'sealName' if that's your field name
    seal_name = serializers.ReadOnlyField(source='sealName') 
    total_price = serializers.SerializerMethodField()

    class Meta:
        model = Sale
        # Ensure 'seal' is changed to 'sealName' here
        fields = ['id', 'sealName', 'seal_name', 'quantity', 'sold_price', 'date_sold', 'total_price']

    def get_total_price(self, obj):
        return obj.quantity * obj.sold_price