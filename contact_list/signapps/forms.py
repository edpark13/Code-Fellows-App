from django import forms
from .models import Info
        
class InfoForm(forms.ModelForm):
    first_name = forms.CharField(max_length=128)
    last_name = forms.CharField(max_length=128, required=False)
    email = forms.EmailField(max_length=128, required=False)
    
    class Meta:
        model = Info
        fields = ('first_name', 'last_name', 'email')