from rest_framework import viewsets
from ..models import Seals, Sale  # Must be 'Seals'
from .serializers import SealsSerializer, SaleSerializer
from django.http import JsonResponse
from ..models import Inventory

class sealsViewSet(viewsets.ModelViewSet):
    queryset = Seals.objects.all() 
    serializer_class = SealsSerializer

class saleViewSet(viewsets.ModelViewSet):
    queryset = Sale.objects.all()
    serializer_class = SaleSerializer
    
def search_seals(request):
    query = request.GET.get("q", "")
    
    results = Inventory.objects.filter(name__icontains=query)

    data = [
        {
            "id": item.id,
            "title": item.name,
            "category": item.category,
            "route": f"/inventory/{item.id}",
        }
        for item in results
    ]

    return JsonResponse(data, safe=False)