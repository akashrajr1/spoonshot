from django import forms

class SearchForm(forms.Form):
	movie = forms.CharField(label='Movie', max_length=15)