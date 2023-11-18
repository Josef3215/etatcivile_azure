from django.db.models import fields
from django import forms
from .models import Persone, Mariage, Deces

class PersoneForm(forms.ModelForm):    
    class Meta:
        model = Persone
        fields = '__all__'

class MariageForm(forms.ModelForm):    
    class Meta:
        model = Mariage
        fields = '__all__' 


class DecesForm(forms.ModelForm):    
    class Meta:
        model = Deces
        fields = '__all__'  


     





