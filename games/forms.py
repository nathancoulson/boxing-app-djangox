from django import forms
from .models import Fight
from .models import Round
from .models import Game
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

class RoundForm(forms.ModelForm):
    game_id = forms.ModelChoiceField(queryset=Game.objects.all())
    round_number = forms.IntegerField(required=True, max_value=12, min_value=1)
    boxer_1_hits = forms.IntegerField(required=True)
    boxer_1_knockdowns = forms.IntegerField(required=True)
    boxer_1_penalties = forms.IntegerField(required=True)
    boxer_2_hits = forms.IntegerField(required=True)
    boxer_2_knockdowns = forms.IntegerField(required=True)
    boxer_2_penalties = forms.IntegerField(required=True)

    class Meta:
        model = Round
        fields = [
            'game_id',
            'round_number',
            'boxer_1_hits',
            'boxer_1_knockdowns',
            'boxer_1_penalties',
            'boxer_2_hits',
            'boxer_2_knockdowns',
            'boxer_2_penalties'
        ]
