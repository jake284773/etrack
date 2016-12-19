from django.views.generic.edit import CreateView

from qualification.forms import QualificationForm
from qualification.models import Qualification


class QualificationCreate(CreateView):
    model = Qualification
    form_class = QualificationForm
