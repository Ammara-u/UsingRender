from rest_framework import viewsets, status
from rest_framework.decorators import action
from rest_framework.response import Response
from django.db.models import Q

from ..models import Seals, Sale
from .serializers import SealsSerializer, SaleSerializer


class SealsViewSet(viewsets.ModelViewSet):
    queryset = Seals.objects.all()
    serializer_class = SealsSerializer

    @action(detail=False, methods=["get"])
    def search(self, request):
        try:
            q = request.query_params.get("q", "").strip()
            
            if not q:
                return Response([])

            # Search across multiple fields
            seals = Seals.objects.filter(
                Q(nameOfSeal__icontains=q) |      # Search by name
                Q(description__icontains=q) |      # Search by description
                Q(partCode__icontains=q)           # Search by part code
            )[:20]  # Limit to 20 results
            
            # Transform results to match frontend interface
            results = []
            for seal in seals:
                results.append({
                    "id": seal.id,
                    "title": seal.nameOfSeal,
                    "category": "Seal",
                    "route": f"/{seal.id}"
                })
            
            return Response(results, status=status.HTTP_200_OK)
            
        except Exception as e:
            return Response(
                {"error": str(e)}, 
                status=status.HTTP_500_INTERNAL_SERVER_ERROR
            )


class SaleViewSet(viewsets.ModelViewSet):
    queryset = Sale.objects.all()
    serializer_class = SaleSerializer