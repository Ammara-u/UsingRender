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
    # Fetch all items from your database
    data = Seals.objects.all()
    
    # Convert QuerySet to a list and send as JSON
    return JsonResponse(list(data), safe=False)

def search_seals(request):
    query = request.GET.get("q", "")

    results = Seals.objects.filter(name__icontains=query)

    data = [
        {
            "id": seal.id,
            "name": seal.name,
        }
        for seal in results
    ]

    return JsonResponse(data, safe=False)