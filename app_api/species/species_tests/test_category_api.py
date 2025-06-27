from django.urls import reverse
from rest_framework import status
from rest_framework.test import APITestCase
from species.models import Category


class SpeciesAPITest(APITestCase):
    def setUp(self):
        self.category_data = Category.objects.create(
            name="Reptile",
            description="Reptiles are mammals that live in water."
        )
        self.list_url = reverse('category-list-create')
        self.detail_url = reverse('category-retrieve-update-destroy', kwargs={'pk': self.category_data.pk})

    def test_list_species(self):
        response = self.client.get(self.list_url)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(Category.objects.count(), 1)

    def test_create_species(self):
        response = self.client.post(self.list_url, data={'name': 'Poultry', 'description': 'Poultry are birds that live on land'})
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertEqual(Category.objects.count(), 2)

    def test_retrieve_species(self):
        response = self.client.get(self.detail_url)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(Category.objects.count(), 1)
        self.assertEqual(Category.objects.first().name, "Reptile")
        self.assertEqual(Category.objects.first().description, "Reptiles are mammals that live in water.")

    def test_update_species(self):
        response = self.client.put(self.detail_url, data={'name': 'Reptile', 'description': 'Reptile is a Dragon'})
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(Category.objects.count(), 1)
        self.assertEqual(Category.objects.first().name, "Reptile")
        self.assertEqual(Category.objects.first().description, "Reptile is a Dragon")

    def test_delete_species(self):
        response = self.client.delete(self.detail_url)
        self.assertEqual(response.status_code, status.HTTP_204_NO_CONTENT)
        self.assertEqual(Category.objects.count(), 0)

    def test_invalid_data(self):
        response = self.client.post(self.list_url, data={'name': 'Reptile,ReptileReptile,ReptileReptile,ReptileReptile,ReptileReptile,ReptileReptile,ReptileReptile,ReptileReptile,ReptileReptile,ReptileReptile,ReptileReptile,ReptileReptile,ReptileReptile,ReptileReptile,ReptileReptile,ReptileReptile,ReptileReptile,ReptileReptile,ReptileReptile,ReptileReptile,ReptileReptile,ReptileReptile,ReptileReptile,ReptileReptile,ReptileReptile,ReptileReptile,ReptileReptile,ReptileReptile,ReptileReptile,ReptileReptile,ReptileReptile,ReptileReptile,Reptile100chars'})
        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)

    def test_patch_name(self):
        response = self.client.patch(self.detail_url, data={'name': 'WaterReptile'})
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(Category.objects.first().name, "WaterReptile")
        self.category_data.refresh_from_db()
        self.assertEqual(self.category_data.name, "WaterReptile")

