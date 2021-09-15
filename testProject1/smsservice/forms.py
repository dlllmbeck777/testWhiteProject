from django import forms
from .models import SmsCodeModel

# creating our forms
class PersonLeadForm(forms.ModelForm):
    sms_code = forms.IntegerField()

    class Meta:
        model = SmsCodeModel
        fields = ('sms_code',)