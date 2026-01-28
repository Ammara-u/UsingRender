from rest_framework import viewsets
from ..models import Seals, Sale  # Must be 'Seals'
from .serializers import SealsSerializer, SaleSerializer

class sealsViewSet(viewsets.ModelViewSet):
    queryset = Seals.objects.all() 
    serializer_class = SealsSerializer

class saleViewSet(viewsets.ModelViewSet):
    queryset = Sale.objects.all()
    serializer_class = SaleSerializer