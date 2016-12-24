from django.test.testcases import TestCase
from django.urls import reverse

from misc.models import SubjectSector
from qualification.models import Unit


class UnitViewTests(TestCase):
    fixtures = ['subjectsector']

    def setUp(self):
        it_sector = SubjectSector.objects.get(name='Information Technology')

        Unit(code='M/601/7261', number=2, name='Computer Systems', level=3,
             glh=60, credits=10, subject_sector=it_sector).save()

    def testListOkay(self):
        response = self.client.get(reverse('qualification:unit:list'))
        self.assertEquals(response.status_code, 200)

    def testDetail(self):
        unit = Unit.objects.get(code='M/601/7261')
        response = self.client.get(reverse('qualification:unit:detail',
                                           kwargs={'pk': unit.pk}))
        self.assertEquals(response.status_code, 200)
        self.assertEquals(response.context['unit'], unit)

    def testDetailThrows404WithInvalidUnit(self):
        response = self.client.get(reverse('qualification:unit:detail',
                                           kwargs={'pk': 500}))
        self.assertEquals(response.status_code, 404)

    def testCreateOkay(self):
        response = self.client.get(reverse('qualification:unit:create'))
        self.assertEquals(response.status_code, 200)

    def testCreatePost(self):
        subject_sector = SubjectSector.objects.get(name='Information '
                                                        'Technology')
        response = self.client.post(reverse('qualification:unit:create'),
                                    data={'code': 'F/601/7233',
                                          'number': 1,
                                          'name': "Communication and "
                                                  "Employability Skills for IT",
                                          'level': 3,
                                          'glh': 60,
                                          'subject_sector': subject_sector.pk,
                                          'credits': 10}, follow=True)
        unit = Unit.objects.get(code='F/601/7233')
        self.assertRedirects(response, reverse('qualification:unit:detail',
                                               kwargs={'pk': unit.pk}))
        self.assertEquals(response.context['unit'], unit)
