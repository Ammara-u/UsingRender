from django.shortcuts import render

# Create your views here.
# views.py
from django.http import JsonResponse
from .models import Seals  # Import your actual model

from django.views.decorators.csrf import csrf_exempt
import json

@csrf_exempt
def seals_list_or_create(request):
    if request.method == 'GET':
        data = Seals.objects.all().values()
        return JsonResponse(list(data), safe=False)
    
    if request.method == 'POST':
        new_data = json.loads(request.body)
        seal = Seals.objects.create(**new_data)
        return JsonResponse({"id": seal.id, "nameOfSeal": seal.nameOfSeal}, status=201)

def inventory_data(request):
    # Use .values() to get simple dictionaries that JSON can understand
    data = list(Seals.objects.all().values())
    return JsonResponse(data, safe=False)


def search_seals(request):
    query = request.GET.get("q", "")

    # 1. Use 'nameOfSeal' instead of 'name'
    results = Seals.objects.filter(nameOfSeal__icontains=query)

    data = [
        {
            "id": seal.partCode,
            "name": seal.nameOfSeal, # 2. Use 'nameOfSeal' here too
        }
        for seal in results
    ]

    return JsonResponse(data, safe=False)