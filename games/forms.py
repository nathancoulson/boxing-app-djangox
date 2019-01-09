from django import forms
from .models import Fight
from datetime import datetime

class FightForm(forms.ModelForm):
    boxer_1 = forms.CharField(max_length=100)
    boxer_2 = forms.CharField(max_length=100)
    fight_date = forms.DateTimeField(initial=datetime.now(), required=False)

    class Meta:
        model = Fight
        fields = [
            'boxer_1',
            'boxer_2',
            'fight_date'
        ]
