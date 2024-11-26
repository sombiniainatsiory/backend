
#urls formulaire JOB
from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import OffreViewSet

from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import OffreViewSet, FormulaireViewSet

# Créez un routeur et enregistrez les ViewSets
router = DefaultRouter()
router.register(r'offres', OffreViewSet)  # Route pour les offres d'emploi
router.register(r'candidatures', FormulaireViewSet)  # Route pour les candidatures

# Inclure les routes générées par le routeur
urlpatterns = [
    path('', include(router.urls)),
]
