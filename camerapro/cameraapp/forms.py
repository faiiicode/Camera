from django import forms
from . models import Callback

class Callform(forms.ModelForm):
    class Meta:
        model=Callback
        fields=['name','email','Phone','message']