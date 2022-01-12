from django import forms
from .models import Talaba
CHOICES =(
    ("+", "+"),
    ("-", "-"),
)

class DavomatForm(forms.Form):
    # name = forms.CharField(max_length=15)
    # surname = forms.CharField(max_length=15)
    status = forms.ChoiceField(choices = CHOICES)
    # date = forms.DateField(input_formats='%Y-%m-%d')
    