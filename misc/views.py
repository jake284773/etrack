from django.urls.base import reverse_lazy
from django.views.generic.detail import DetailView
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.views.generic.list import ListView

from misc.models import SubjectSector, Faculty


class SubjectSectorList(ListView):
    model = SubjectSector
    context_object_name = 'subject_sectors'


class SubjectSectorCreate(CreateView):
    model = SubjectSector
    fields = ['number', 'name']


class SubjectSectorUpdate(UpdateView):
    model = SubjectSector
    fields = ['number', 'name']
    template_name_suffix = '_update_form'


class SubjectSectorDetail(DetailView):
    model = SubjectSector


class SubjectSectorDelete(DeleteView):
    model = SubjectSector
    success_url = reverse_lazy('misc:subject-sector:list')


class FacultyList(ListView):
    model = Faculty
    context_object_name = 'faculties'


class FacultyCreate(CreateView):
    model = Faculty
    fields = ['code', 'name']


class FacultyUpdate(UpdateView):
    model = Faculty
    fields = ['code', 'name']
    context_object_name = 'faculty'
    template_name_suffix = '_update_form'


class FacultyDetail(DetailView):
    model = Faculty
    context_object_name = 'faculty'


class FacultyDelete(DeleteView):
    model = Faculty
    context_object_name = 'faculty'
    success_url = reverse_lazy('misc:faculty:list')
