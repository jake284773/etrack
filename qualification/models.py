from django.db import models
from django.urls import reverse

from misc.models import SubjectSector


class Qualification(models.Model):
    LEVELS = (
        (2, 'Level 2'),
        (3, 'Level 3'),
    )

    FRAMEWORKS = (
        ('QCF', 'QCF (Qualifications and Credit Framework)'),
        ('NQF', 'NQF (National Qualification Framework)'),
    )

    qn = models.CharField(max_length=10, verbose_name='qualification number',
                          unique=True)
    name = models.CharField(max_length=50)
    level = models.IntegerField(choices=LEVELS, default=3)
    glh = models.IntegerField(verbose_name='guided learning hours')
    framework = models.CharField(max_length=3, choices=FRAMEWORKS,
                                 default='QCF')
    total_credits = models.IntegerField()

    def __str__(self):
        return self.name + ' (' + self.qn + ')'

    def get_absolute_url(self):
        return reverse('qualification:detail', kwargs={'pk': self.pk})


class Pathway(models.Model):
    qualification = models.ForeignKey('Qualification')
    name = models.CharField(max_length=50, default='N/A',
                            help_text="If the qualification has only one "
                                      "unnamed pathway, leave this field "
                                      "as N/A.")
    subject_sector = models.ForeignKey(SubjectSector)
    units = models.ManyToManyField('Unit', through='PathwayUnit')
    mandatory_credits = models.IntegerField()
    optional_credits = models.IntegerField()

    def get_absolute_url(self):
        return reverse('qualification:pathway:detail',
                       kwargs={'qualification_id':
                                   self.kwargs['qualification_id'],
                               'pk': self.pk})


class QualificationGrade(models.Model):
    class Meta:
        unique_together = ('qualification', 'grade')

    qualification = models.ForeignKey('Qualification')
    grade = models.CharField(max_length=6)
    full_grade = models.CharField(max_length=50)
    points_start = models.IntegerField()
    points_end = models.IntegerField(blank=True, null=True)
    ucas_points = models.IntegerField(blank=True, null=True)


class PathwayUnit(models.Model):
    class Meta:
        unique_together = ('pathway', 'unit')

    pathway = models.ForeignKey('Pathway')
    unit = models.ForeignKey('Unit')
    number_override = models.IntegerField(blank=True, null=True)
    mandatory = models.BooleanField()


class Unit(models.Model):
    code = models.CharField(max_length=10, unique=True)
    number = models.IntegerField()
    name = models.CharField(max_length=50)
    credits = models.IntegerField()
    glh = models.IntegerField(verbose_name='guided learning hours')
    level = models.IntegerField(default=3, choices=Qualification.LEVELS)
    subject_sector = models.ForeignKey(SubjectSector)

    def get_absolute_url(self):
        return reverse('qualification:unit:detail', kwargs={'pk': self.pk})

    def __str__(self):
        return 'Unit ' + str(self.number) + ' - ' + self.name


class Criteria(models.Model):
    class Meta:
        unique_together = ('unit', 'number')

    unit = models.ForeignKey('Unit')
    number = models.CharField(max_length=3)
    description = models.CharField(max_length=255)
