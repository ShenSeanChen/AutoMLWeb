from django import forms
from regression.models import csvInput

class NewDataForm(forms.ModelForm):
    class Meta:
        model = csvInput
        fields = '__all__'
    
