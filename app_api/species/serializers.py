from rest_framework import serializers
from .models import ProtectedSpecies

class ProtectedSpeciesSerializer(serializers.ModelSerializer):
    class Meta:
        model = ProtectedSpecies
        fields = '__all__'

    def validate_population(self, value):
        if value < 0:
            raise serializers.ValidationError("Population must be greater than 0")
        return value