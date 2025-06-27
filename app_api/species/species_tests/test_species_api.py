from django.urls import reverse
from rest_framework import status
from rest_framework.test import APITestCase
from species.models import Species, Category


class SpeciesAPITest(APITestCase):
    def setUp(self):
        self.category_data = Category.objects.create(
            name="Reptile",
            description="Reptiles are mammals that live in water."
        )
        self.species_data = Species.objects.create(
            name="Black Mamba",
            classification="Snake",
            population=700,
            is_protected=False,
            category=self.category_data
        )
        self.list_url = reverse('species-list-create')
        self.detail_url = reverse('species-retrieve-update-destroy', kwargs={'pk': self.species_data.pk})

    def test_list_species(self):
        response = self.client.get(self.list_url)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(Species.objects.count(), 1)

    def test_create_species(self):
        response = self.client.post(self.list_url, data={'name': 'Red Mamba', 'classification': 'Snake', 'population': 10, 'is_protected': True, 'category': self.category_data.pk})
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertEqual(Species.objects.count(), 2)

    def test_retrieve_species(self):
        response = self.client.get(self.detail_url)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(Species.objects.count(), 1)
        self.assertEqual(Species.objects.first().name, "Black Mamba")
        self.assertEqual(Species.objects.first().classification, "Snake")
        self.assertEqual(Species.objects.first().population, 700)
        self.assertEqual(Species.objects.first().is_protected, False)
        self.assertEqual(Species.objects.first().category.name, "Reptile")

    def test_update_species(self):
        response = self.client.put(self.detail_url, data={'name': 'Red Mamba', 'classification': 'Snake', 'population': 100001, 'is_protected': False, 'category': self.category_data.pk})
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(Species.objects.count(), 1)
        self.assertEqual(Species.objects.first().name, "Red Mamba")
        self.assertEqual(Species.objects.first().classification, "Snake")
        self.assertEqual(Species.objects.first().population, 100001)
        self.assertEqual(Species.objects.first().is_protected, False)
        self.assertEqual(Species.objects.first().category.name, "Reptile")

    def test_delete_species(self):
        response = self.client.delete(self.detail_url)
        self.assertEqual(response.status_code, status.HTTP_204_NO_CONTENT)
        self.assertEqual(Species.objects.count(), 0)

    def test_invalid_data(self):
        response = self.client.post(self.list_url, data={'name': 'Red Mamba'})
        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)

    def test_patch_population(self):
        response = self.client.patch(self.detail_url, data={'population': 100})
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(Species.objects.first().population, 100)
        self.species_data.refresh_from_db()
        self.assertEqual(self.species_data.population, 100)

