from django.db import models

# Create your models here.
class ProtectedSpecies(models.Model):
    name = models.CharField(max_length=100)
    classification = models.CharField(max_length=100)
    population = models.IntegerField()