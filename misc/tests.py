from django.test import RequestFactory
from django.test import TestCase
from django.urls import reverse

from misc.models import SubjectSector


class SubjectSectorModel(TestCase):
    def test_str(self):
        subject_sector = SubjectSector(number=150, name="Test One Fifty Zero Sector")
        self.assertEquals(str(subject_sector), "Test One Fifty Zero Sector (150)")


class SubjectSectorViewsTest(TestCase):
    def setUp(self):
        self.factory = RequestFactory()

    def test_list_okay(self):
        response = self.client.get(reverse('misc:subject-sector:list'))
        self.assertEquals(response.status_code, 200)

    def test_create_okay(self):
        response = self.client.get(reverse('misc:subject-sector:create'))
        self.assertEquals(response.status_code, 200)

    def test_list_contains_one_sector(self):
        subject_sector = SubjectSector(number=100, name='Test Sector')
        subject_sector.save()

        response = self.client.get(reverse('misc:subject-sector:list'))
        self.assertEquals(response.status_code, 200)
        self.assertContains(response, 'Test Sector')
        self.assertContains(response, '100')

    def test_create_submit(self):
        self.test_create_okay()
        response = self.client.post(reverse('misc:subject-sector:create'), {'number': 100, 'name': 'Test Sector'},
                                    follow=True)
        created_subject_sector = SubjectSector.objects.get(number=100)
        new_subject_sector_url = reverse('misc:subject-sector:detail', kwargs={'pk': created_subject_sector.pk})
        self.assertRedirects(response, new_subject_sector_url)
        self.assertContains(response, 'Test Sector')

    def test_update(self):
        new_name = "Test Sector Two"

        subject_sector = SubjectSector(number=101, name='Test Sector One')
        subject_sector.save()
        update_response = self.client.post(reverse('misc:subject-sector:update', kwargs={'pk': subject_sector.pk}),
                                           {'number': 101, 'name': new_name}, follow=True)
        self.assertRedirects(update_response, reverse('misc:subject-sector:detail', kwargs={'pk': subject_sector.pk}))
        self.assertContains(update_response, new_name)

    def test_delete(self):
        sector_name = 'Test Sector Two'
        subject_sector = SubjectSector(number=102, name=sector_name)
        subject_sector.save()
        delete_get_response = self.client.get(reverse('misc:subject-sector:delete', kwargs={'pk': subject_sector.pk}))
        self.assertEquals(delete_get_response.status_code, 200)
        delete_response = self.client.post(reverse('misc:subject-sector:delete', kwargs={'pk': subject_sector.pk}),
                                           follow=True)
        self.assertRedirects(delete_response, reverse('misc:subject-sector:list'))
        self.assertNotContains(delete_response, sector_name)
