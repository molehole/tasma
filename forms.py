from django import forms

class terminal(forms.Form):
    etykieta = forms.ChoiceField()
    kod = forms.IntegerField()
