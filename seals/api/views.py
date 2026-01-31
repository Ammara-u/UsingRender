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
            # Return dummy data to test if the endpoint works
            return Response([
                {
                    "id": 1,
                    "title": "Test Seal",
                    "category": "Seal",
                    "route": "/seal/1"
                }
            ])


class SaleViewSet(viewsets.ModelViewSet):
    queryset = Sale.objects.all()
    serializer_class = SaleSerializer