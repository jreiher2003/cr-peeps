from django import forms 

class NFLCreateBet(forms.Form):
    away_team = forms.CharField()
    home_team = forms.CharField()
    team = forms.ChoiceField()
    point_spread = forms.IntegerField(min_value=-14,max_value=14)
    totals = forms.IntegerField(min_value=30, max_value=80) 