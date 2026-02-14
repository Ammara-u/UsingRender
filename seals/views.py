from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
from .models import Seals
import json


@csrf_exempt
def seals_list_or_create(request):

    if request.method == 'GET':
        data = list(Seals.objects.all().values())
        return JsonResponse(data, safe=False)

    if request.method == 'POST':
        new_data = json.loads(request.body)

        seal = Seals.objects.create(
            partCode=new_data.get("partCode"),
            description=new_data.get("description"),
            price=new_data.get("price"),
            stock=new_data.get("stock", 0),
            minStock=new_data.get("minStock", 500)
        )

        return JsonResponse({
            "id": seal.id,
            "partCode": seal.partCode
        }, status=201)


def search_seals(request):
    query = request.GET.get("q", "")
    results = Seals.objects.filter(partCode__icontains=query)

    data = [
        {
            "id": seal.id,
            "name": seal.partCode,
        }
        for seal in results
    ]

    return JsonResponse(data, safe=False)
