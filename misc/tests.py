from django.test import RequestFactory
from django.test import TestCase
from django.urls import reverse

from misc.models import SubjectSector, Faculty


class ResponseTestCase(TestCase):
    def assertResponseOkay(self, url):
        response = self.client.get(reverse(url))
        self.assertEquals(response.status_code, 200)


class SubjectSectorModel(TestCase):
    def test_str(self):
        subject_sector = SubjectSector(number=150, name="Test One Fifty Zero Sector")
        self.assertEquals(str(subject_sector), "Test One Fifty Zero Sector (150)")


class SubjectSectorViewsTest(ResponseTestCase):
    def setUp(self):
        self.factory = RequestFactory()

    def testListOkay(self):
        self.assertResponseOkay('misc:subject-sector:list')

    def testListContainsOneSector(self):
        subject_sector = SubjectSector(number=100, name='Test Sector')
        subject_sector.save()

        response = self.client.get(reverse('misc:subject-sector:list'))
        self.assertContains(response, 'Test Sector')
        self.assertContains(response, '100')

    def testCreateOkay(self):
        self.assertResponseOkay('misc:subject-sector:create')

    def testCreateSubmit(self):
        self.testCreateOkay()
        response = self.client.post(reverse('misc:subject-sector:create'), {'number': 100, 'name': 'Test Sector'},
                                    follow=True)
        created_subject_sector = SubjectSector.objects.get(number=100)
        new_subject_sector_url = reverse('misc:subject-sector:detail', kwargs={'pk': created_subject_sector.pk})
        self.assertRedirects(response, new_subject_sector_url)
        self.assertContains(response, 'Test Sector')

    def testUpdate(self):
        new_name = "Test Sector Two"

        subject_sector = SubjectSector(number=101, name='Test Sector One')
        subject_sector.save()
        update_response = self.client.post(reverse('misc:subject-sector:update', kwargs={'pk': subject_sector.pk}),
                                           {'number': 101, 'name': new_name}, follow=True)
        self.assertRedirects(update_response, reverse('misc:subject-sector:detail', kwargs={'pk': subject_sector.pk}))
        self.assertContains(update_response, new_name)

    def testDelete(self):
        sector_name = 'Test Sector Two'
        subject_sector = SubjectSector(number=102, name=sector_name)
        subject_sector.save()
        delete_get_response = self.client.get(reverse('misc:subject-sector:delete', kwargs={'pk': subject_sector.pk}))
        self.assertEquals(delete_get_response.status_code, 200)
        delete_response = self.client.post(reverse('misc:subject-sector:delete', kwargs={'pk': subject_sector.pk}),
                                           follow=True)
        self.assertRedirects(delete_response, reverse('misc:subject-sector:list'))
        self.assertNotContains(delete_response, sector_name)


class FacultyViewsTests(ResponseTestCase):
    def testListOkay(self):
        self.assertResponseOkay('misc:faculty:list')

    def testListOneFaculty(self):
        faculty = Faculty(code='CCDI', name='Creative Cultural and Digital Industries')
        faculty.save()

        response = self.client.get(reverse('misc:faculty:list'))
        # self.assertContains(response, '<td>CCDI</td>\n<td>Creative Cultural and Digital Industries</td>', html=True)
        self.assertContains(response, "Creative Cultural and Digital Industries")

    def testCreateOkay(self):
        self.assertResponseOkay('misc:faculty:create')
