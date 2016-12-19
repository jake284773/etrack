from django.core.exceptions import ValidationError
from django.core.validators import RegexValidator
from django.db import models

from misc.models import SubjectSector


class Qualification(models.Model):
    SUPPORTED_LEVELS = (
        (2, 'Level 2'),
        (3, 'Level 3'),
    )

    class Meta:
        unique_together = ('qn', 'pathway')

    qn = models.CharField(max_length=10, verbose_name='qualification number',
                          validators=[
                              RegexValidator(
                                  regex='([A-Z])\/([0-9]){4}\/([0-9]){3}',
                                  message='Invalid qualification number. '
                                          'Must follow F/3495/239 example.',
                                  code='invalid_qn'
                              )
                          ])
    name = models.CharField(max_length=50)
    pathway = models.CharField(max_length=50, null=True, blank=True)
    level = models.IntegerField(choices=SUPPORTED_LEVELS, default=3)
    glh = models.IntegerField(verbose_name='guided learning hours')
    subject_sector = models.ForeignKey(SubjectSector)
    total_credits = models.IntegerField(validators=['validate_total_credits'])
    mandatory_credits = models.IntegerField()
    optional_credits = models.IntegerField()
    units = models.ManyToManyField('Unit', through='QualificationUnit', limit_choices_to={'subject_sector': subject_sector})

    def validate_total_credits(self):
        if (self.mandatory_credits + self.optional_credits) != self.total_credits:
            raise ValidationError("Total credits must add up to mandatory and optional credits")

    def __str__(self):
        return self.name + " (" + self.pathway + ")"


class QualificationGrade(models.Model):
    class Meta:
        unique_together = ('qualification', 'grade')

    qualification = models.ForeignKey('Qualification')
    grade = models.CharField(max_length=6)
    description = models.CharField(max_length=50)
    points_start = models.IntegerField()
    points_end = models.IntegerField(blank=True, null=True)
    ucas_points = models.IntegerField(blank=True, null=True)


class QualificationUnit(models.Model):
    class Meta:
        unique_together = ('qualification', 'unit', 'number')

    qualification = models.ForeignKey('Qualification')
    unit = models.ForeignKey('Unit')
    number = models.IntegerField()
    mandatory = models.BooleanField()


class Unit(models.Model):
    code = models.CharField(max_length=10, unique=True)
    name = models.CharField(max_length=50)
    credits = models.IntegerField()
    glh = models.IntegerField()
    level = models.IntegerField()
    subject_sector = models.ForeignKey(SubjectSector)


class Criteria(models.Model):
    class Meta:
        unique_together = ('unit', 'number')

    unit = models.ForeignKey('Unit')
    number = models.CharField(max_length=3)
    description = models.CharField(max_length=255)
