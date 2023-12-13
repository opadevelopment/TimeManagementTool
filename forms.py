from django import forms

from .models import Kurssi, Teht

class KurssiForm(forms.ModelForm):
    class Meta:
        model = Kurssi
        fields = ['kurssi']
        labels = {'kurssi': ''}

class TehtForm(forms.ModelForm):

    class Meta:
        model = Teht
        valmis = forms.BooleanField(initial = True, required = False)
        fields = ['teht', 'dedis', 'valmis']
        labels = {'teht': ''}
        widgets = {'dedis': forms.DateInput(attrs={'type': 'date', 'placeholder':'dd-mm-yyy (DOB)', 'class': 'form-control'})}
