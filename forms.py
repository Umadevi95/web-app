from django import forms
from .models import *


class ckdForm(forms.ModelForm):
    class Meta():
        model=ckdModel
        fields=['no_of_dependents', 'loan_amount', 'loan_term', 'cibil_score']
