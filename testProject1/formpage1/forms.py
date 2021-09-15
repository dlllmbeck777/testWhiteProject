# importing forms
from django import forms
from .models import PersonPage,Leads

# creating our forms
class PersonLeadForm(forms.ModelForm):    
    iin = forms.CharField(max_length=12,required=True)
    phone = forms.CharField(max_length=20,required=True)
    is_gathering = forms.BooleanField(required=True,initial=False)

    class Meta:
        model = Leads
        fields = ('iin','phone','is_gathering')