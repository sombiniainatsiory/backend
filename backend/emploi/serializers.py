from rest_framework import serializers
from .models import Offre
from .models import Formulaire

#serializers de formulaireJOB
class OffreSerializer(serializers.ModelSerializer):
    class Meta:
        model = Offre
        fields = ['titre_offre', 'nom_entreprise', 'activite', 'missions', 'profil', 'reference']


#serializers de formulaireCV
class FormulaireSerializer(serializers.ModelSerializer):
    class Meta:
        model = Formulaire
        fields = ['id', 'titre', 'cursus', 'experience', 'competence', 'langue', 'softskills','motivation',
                  'reference']
