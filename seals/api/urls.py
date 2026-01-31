from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import sealsViewSet, saleViewSet
from .views import search_seals
# Use this specific name 'seals_router' to fix the ImportError you had earlier
seals_router = DefaultRouter()
seals_router.register(r'seals', sealsViewSet)
seals_router.register(r'sales', saleViewSet) # This registers the /api/sales/ path

urlpatterns = [
    path('', include(seals_router.urls)),
    path("search/", search_seals, name="search_seals"),

]