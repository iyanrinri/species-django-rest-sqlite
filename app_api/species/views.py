from django.shortcuts import render
from rest_framework import generics, viewsets
from .serializers import ProtectedSpeciesSerializer
from .models import ProtectedSpecies
# Create your views here.

class ProtectedSpeciesListCreateView(generics.ListCreateAPIView):
    queryset = ProtectedSpecies.objects.all()
    serializer_class = ProtectedSpeciesSerializer

class ProtectedSpeciesRetrieveUpdateDestroyView(generics.RetrieveUpdateDestroyAPIView):
    queryset = ProtectedSpecies.objects.all()
    serializer_class = ProtectedSpeciesSerializer