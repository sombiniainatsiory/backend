from django.shortcuts import render
from .models import Formulaire, Offre
from .serializers import FormulaireSerializer, OffreSerializer
from rest_framework import  viewsets
# Create your views here.


# views de formulaire CV
class FormulaireViewSet(viewsets.ModelViewSet):
    queryset = Formulaire.objects.all()
    serializer_class = FormulaireSerializer



# views de formulaire JOB
class OffreViewSet(viewsets.ModelViewSet):
    queryset = Offre.objects.all()
    serializer_class = OffreSerializer
    