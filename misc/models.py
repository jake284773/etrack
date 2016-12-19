from django.db import models
from django.urls import reverse


class SubjectSector(models.Model):
    number = models.IntegerField(unique=True)
    name = models.CharField(max_length=50)

    def __str__(self):
        return self.name + " (" + str(self.number) + ")"

    def get_absolute_url(self):
        return reverse('misc:subject-sector:detail', kwargs={'pk': self.pk})


class Faculty(models.Model):
    code = models.CharField(max_length=5, unique=True)
    name = models.CharField(max_length=50)

    def __str__(self):
        return self.name + " (" + self.code + ")"

    def get_absolute_url(self):
        return reverse('misc:faculty:detail', kwargs={'pk': self.pk})