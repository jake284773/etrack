from django.db import models
from django.contrib.auth.models import User

from misc.models import SubjectSector, Faculty
from qualification.models import QualificationUnit, Qualification


class Course(models.Model):
    code = models.CharField(max_length=10)
    name = models.CharField(max_length=50)
    qualification = models.ForeignKey(Qualification)
    units = models.ManyToManyField(QualificationUnit)
    start_date = models.DateField()
    end_date = models.DateField()
    subject_sector = models.ForeignKey(SubjectSector)
    faculty = models.ForeignKey(Faculty)
    course_organiser = models.ForeignKey(User)
    students = models.ManyToManyField(User, through='CourseStudent', related_name='course_students')


class CourseStudent(models.Model):
    course = models.ForeignKey('Course')
    student = models.ForeignKey(User)
    final_grade = models.CharField(max_length=6, blank=True, null=True)
    predicted_grade = models.CharField(max_length=6, blank=True, null=True)
    target_grade = models.CharField(max_length=6, blank=True, null=True)
    final_ucas_points = models.IntegerField(blank=True, null=True)
    predicted_ucas_points = models.IntegerField(blank=True, null=True)


class StudentGroup(models.Model):
    course = models.ForeignKey('Course')
    tutor = models.ForeignKey(User, related_name='tutor')
    students = models.ManyToManyField(User, related_name='group_students')
