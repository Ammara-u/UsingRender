from rest_framework import viewsets
from rest_framework.decorators import action
from rest_framework.response import Response

from ..models import Seals, Sale
from .serializers import SealsSerializer, SaleSerializer


class SealsViewSet(viewsets.ModelViewSet):
    queryset = Seals.objects.all()
    serializer_class = SealsSerializer

    @action(detail=False, methods=["get"])
    def search(self, request):
        q = request.query_params.get("q", "").strip()

        if not q:
            return Response([])

        seals = Seals.objects.filter(NameOfSeal__icontains=q)
        
        # Transform the results to match your frontend interface
        results = []
        for seal in seals:
            results.append({
                "id": seal.id,
                "title": seal.NameOfSeal,
                "category": "Seal",  # or use a field from your model
                "route": f"/seal-detail/{seal.id}"  # Adjust route as needed
            })
        
        return Response(results)


class SaleViewSet(viewsets.ModelViewSet):
    queryset = Sale.objects.all()
    serializer_class = SaleSerializer