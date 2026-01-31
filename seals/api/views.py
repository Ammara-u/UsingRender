from rest_framework import viewsets
from rest_framework.decorators import action
from rest_framework.response import Response

from ..models import Seal, Sale
from .serializers import SealSerializer, SaleSerializer


class SealsViewSet(viewsets.ModelViewSet):
    queryset = Seal.objects.all()
    serializer_class = SealSerializer

    @action(detail=False, methods=["get"])
    def search(self, request):
        q = request.query_params.get("q", "").strip()

        if not q:
            return Response([])

        seals = Seal.objects.filter(NameOfSeal__icontains=q)
        serializer = self.get_serializer(seals, many=True)
        return Response(serializer.data)


class SaleViewSet(viewsets.ModelViewSet):
    queryset = Sale.objects.all()
    serializer_class = SaleSerializer
