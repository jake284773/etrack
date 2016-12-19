from django.forms import ModelForm
from django.forms.widgets import RadioSelect

from qualification.models import Qualification


class QualificationForm(ModelForm):
    class Meta:
        model = Qualification
        fields = ['qn', 'name', 'pathway', 'level', 'glh', 'total_credits',
                  'mandatory_credits', 'optional_credits']
        widgets = {
            'level': RadioSelect()
        }