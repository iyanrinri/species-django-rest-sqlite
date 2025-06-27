from rest_framework import serializers
from .models import Species, Category

class SpeciesSerializer(serializers.ModelSerializer):
    class Meta:
        model = Species
        fields = '__all__'

    def validate_population(self, value):
        if value < 0:
            raise serializers.ValidationError("Population must be greater than 0")
        return value

class CategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = Category
        fields = '__all__'

    def validate_name(self, value):
        if len(value) == 0:
            raise serializers.ValidationError("Category name is required")
        if len(value) > 100:
            raise serializers.ValidationError("Category name length must not more than 100")
        if not value.strip():
            raise serializers.ValidationError("Category name must not contain spaces")
        return value