from django import forms
from .models import FamilyMember

class FamilyForm(forms.ModelForm):
    class Meta:
        model = FamilyMember
        fields = [
            'name',
            'parent',
            'siblings'
        ]

class RawFamilyForm(forms.Form):
    name = forms.CharField()
    parent = forms.CharField()
    siblings = forms.CharField()