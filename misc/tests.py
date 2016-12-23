from django.test import RequestFactory, TestCase
from django.urls import reverse

from misc.models import SubjectSector, Faculty


class ResponseTestCase(TestCase):
    def assertResponseOkay(self, url):
        response = self.client.get(reverse(url))
        self.assertEquals(response.status_code, 200)


class SubjectSectorModel(TestCase):
    def testStr(self):
        subject_sector = SubjectSector(number=150,
                                       name="Test One Fifty Zero Sector")
        self.assertEquals(str(subject_sector),
                          "Test One Fifty Zero Sector (150)")


class FacultyModel(TestCase):
    def testStr(self):
        faculty = Faculty(code='BM', name='Business Management')
        self.assertEquals(str(faculty), "Business Management (BM)")


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
        response = self.client.post(reverse('misc:subject-sector:create'),
                                    {'number': 100, 'name': 'Test Sector'},
                                    follow=True)
        created_subject_sector = SubjectSector.objects.get(number=100)
        new_subject_sector_url = reverse(
            'misc:subject-sector:detail',
            kwargs={'pk': created_subject_sector.pk}
        )
        self.assertRedirects(response, new_subject_sector_url)
        self.assertContains(response, 'Test Sector')

    def testUpdate(self):
        new_name = "Test Sector Two"

        subject_sector = SubjectSector(number=101, name='Test Sector One')
        subject_sector.save()
        update_response = self.client.post(
            reverse('misc:subject-sector:update',
                    kwargs={'pk': subject_sector.pk}),
            {'number': 101, 'name': new_name},
            follow=True)
        self.assertRedirects(
            update_response,
            reverse('misc:subject-sector:detail',
                    kwargs={'pk': subject_sector.pk})
        )

        self.assertContains(update_response, new_name)

    def testDelete(self):
        SubjectSector(number=102, name='Test Sector Two').save()
        subject_sector = SubjectSector.objects.get(number=102)
        subject_sector_url = reverse('misc:subject-sector:detail',
                                     kwargs={'pk': subject_sector.pk})
        delete_url = reverse('misc:subject-sector:delete',
                             kwargs={'pk': subject_sector.pk})
        response_confirm = self.client.get(delete_url)
        self.assertEquals(response_confirm.status_code, 200)
        response = self.client.post(delete_url, follow=True)
        self.assertRedirects(response,
                             reverse('misc:subject-sector:list'))
        self.assertNotContains(response, subject_sector.name)
        self.assertNotContains(response, '<td><a href="' + subject_sector_url +
                               '">' + str(subject_sector.number) + '</td>')


class FacultyViewsTests(ResponseTestCase):
    def testListOkay(self):
        self.assertResponseOkay('misc:faculty:list')

    def testListOneFaculty(self):
        Faculty(
            code='CCDI', name='Creative Cultural and Digital Industries'
        ).save()
        faculty = Faculty.objects.get(code='CCDI')

        response = self.client.get(reverse('misc:faculty:list'))
        faculty_url = reverse('misc:faculty:detail', kwargs={'pk': faculty.pk})
        self.assertContains(
            response,
            '<td><a href="' + faculty_url + '">' + faculty.code + '</a></td>',
            html=True)
        self.assertContains(response, '<td>' + faculty.name + '</td>',
                            html=True)

    def testCreateOkay(self):
        self.assertResponseOkay('misc:faculty:create')

    def testCreatePost(self):
        response = self.client.post(reverse('misc:faculty:create'),
                                    data={'code': 'BHM',
                                          'name': 'Business Health Management'},
                                    follow=True)
        new_faculty = Faculty.objects.get(code='BHM')
        new_faculty_url = reverse('misc:faculty:detail', kwargs={
            'pk': new_faculty.pk})
        self.assertRedirects(response, new_faculty_url)
        self.assertContains(response, '<h1 class="page-header">' +
                            str(new_faculty) + '</h1>',
                            html=True)

    def testUpdate(self):
        new_name = "Business Management"
        Faculty(code='BHM', name='Business Health Management').save()
        faculty = Faculty.objects.get(code='BHM')

        update_url = reverse('misc:faculty:update', kwargs={'pk': faculty.pk})
        redirect_url = reverse('misc:faculty:detail', kwargs={'pk': faculty.pk})
        response_form = self.client.get(update_url)
        self.assertEquals(response_form.status_code, 200)
        response = self.client.post(update_url,
                                    data={'code': 'BM', 'name': new_name},
                                    follow=True)
        self.assertRedirects(response, redirect_url)
        faculty = Faculty.objects.get(code='BM')
        self.assertContains(response, '<h1 class="page-header">' +
                            str(faculty) + '</h1>',
                            html=True)

    def testDelete(self):
        Faculty(code='BM', name='Business Management').save()
        faculty = Faculty.objects.get(code='BM')
        faculty_url = reverse('misc:faculty:detail', kwargs={'pk': faculty.pk})
        delete_url = reverse('misc:faculty:delete', kwargs={'pk': faculty.pk})

        response_confirm = self.client.get(delete_url)
        self.assertEquals(response_confirm.status_code, 200)
        response = self.client.post(delete_url, follow=True)
        self.assertRedirects(response, reverse('misc:faculty:list'))
        self.assertNotContains(response, 'Business Management')
        self.assertNotContains(response, '<td><a href="' + faculty_url +
                               '">BM</a></td>', html=True)
