from django.forms import ModelForm
from django.forms.widgets import RadioSelect

from qualification.models import Qualification, Unit


class QualificationForm(ModelForm):
    class Meta:
        model = Qualification
        fields = ['qn', 'name', 'level', 'framework', 'glh', 'total_credits']
        widgets = {
            'level': RadioSelect(),
            'framework': RadioSelect(),
        }


class UnitForm(ModelForm):
    class Meta:
        model = Unit
        fields = ['code', 'number', 'name', 'level', 'glh', 'credits',
                  'subject_sector']
        widgets = {
            'level': RadioSelect(),
        }
