

# Register your models here.
from django.contrib import admin
from .models import Formulaire
from .models import Offre

# Enregistrement du modèle dans l'interface admin de formulaire CV
@admin.register(Formulaire)
class FormulaireAdmin(admin.ModelAdmin):
    # Configuration de l'affichage des champs dans la liste admin
    list_display = ('id', 'titre', 'cursus', 'experience', 'competence', 'langue', 'softskills','motivation','reference')
    # Ajout d'une barre de recherche pour certains champs
    search_fields = ('titre', 'cursus', 'competence')
    # Ajout de filtres sur certains champs
    list_filter = ('langue',)



#formulaire JOB

class OffreAdmin(admin.ModelAdmin):
    # Personnalisation de l'affichage dans l'admin
    list_display = ('titre_offre', 'nom_entreprise', 'activite', 'reference')  # Colonnes affichées dans la liste
    search_fields = ('titre_offre', 'nom_entreprise')  # Ajoute une barre de recherche
    list_filter = ('activite',)  # Ajoute des filtres par activité
    ordering = ('titre_offre',)  # Tri par défaut

# Enregistrer le modèle avec sa configuration
admin.site.register(Offre, OffreAdmin)
