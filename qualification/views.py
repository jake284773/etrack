from django.views.generic.detail import DetailView
from django.views.generic.edit import CreateView
from django.views.generic.list import ListView

from qualification.forms import QualificationForm
from qualification.models import Qualification, Pathway


class QualificationList(ListView):
    model = Qualification
    context_object_name = 'qualifications'


class QualificationCreate(CreateView):
    model = Qualification
    form_class = QualificationForm


class QualificationDetail(DetailView):
    model = Qualification
    context_object_name = 'qualification'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['pathways'] = Pathway.objects.filter(qualification=self.kwargs['pk'])
        return context


class PathwayCreate(CreateView):
    model = Pathway
    context_object_name = 'pathway'
    fields = ['name', 'mandatory_credits', 'optional_credits',
              'subject_sector']

    def form_valid(self, form):
        form.instance.qualification = Qualification.objects.get(
            id=self.kwargs['qualification_id'])
        return super().form_valid(form)

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['qualification'] = Qualification.objects.get(
            id=self.kwargs['qualification_id'])
        return context
