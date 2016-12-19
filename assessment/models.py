from django.contrib.auth.models import User
from django.db import models

from qualification.models import Criteria, Unit


class Assignment(models.Model):
    code = models.CharField(max_length=15, unique=True)
    unit = models.ForeignKey(Unit)
    number = models.IntegerField()
    available_date = models.DateTimeField()
    deadline = models.DateTimeField()
    marking_start_date = models.DateTimeField()
    marking_deadline = models.DateTimeField()
    criteria = models.ManyToManyField(Criteria)
    submissions = models.ManyToManyField(User, through='AssignmentSubmission')


class AssignmentSubmission(models.Model):
    assignment = models.ForeignKey('Assignment')
    student = models.ForeignKey(User)
    submission_datetime = models.DateTimeField(verbose_name='submission date')


class CriteriaStudentAssessment(models.Model):
    assignment = models.ForeignKey(Assignment)
    student = models.ForeignKey(User)
    criteria = models.ForeignKey(Criteria)
    assessor = models.ForeignKey(User, related_name='assessor')
    moderator = models.ForeignKey(User, related_name='moderator', blank=True, null=True)
    status = models.CharField(max_length=3)
    last_updated = models.DateTimeField(auto_now=True)
