from django.forms import ModelForm
from django.forms.widgets import RadioSelect

from qualification.models import Qualification


class QualificationForm(ModelForm):
    class Meta:
        model = Qualification
        fields = ['qn', 'name', 'level', 'framework', 'glh', 'total_credits']
        widgets = {
            'level': RadioSelect(),
            'framework': RadioSelect(),
        }
