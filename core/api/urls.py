from django.urls import path, include
# Import 'seals_router' directly
from seals.api.urls import seals_router

urlpatterns = [
    path('', include(seals_router.urls)),
    
]