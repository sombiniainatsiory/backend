from django.db import models

# Modèle pour le formulaireCV
class Formulaire(models.Model):
    titre = models.CharField(max_length=255)
    cursus = models.TextField()
    experience = models.TextField()
    competence = models.TextField()
    langue = models.TextField()
    softskills = models.TextField()
    motivation = models.TextField(default="ma motiavion")
    reference = models.TextField()
    
    def __str__(self):
        return self.titre
    
# Modèle pour le formulaireJob
class Offre(models.Model):
    titre_offre = models.CharField(max_length=255)
    nom_entreprise = models.CharField(max_length=50)
    activite = models.TextField()
    missions = models.TextField()
    profil = models.TextField()
    reference = models.TextField()

    def __str__(self):
        return self.titre_offre