from django import forms
from.models import Restaurant

class CreateForm(forms.Form):
    Name = forms.CharField(label='Restaurant Name', max_length=100, widget=forms.TextInput(attrs={'placeholder': 'Name', 'style': 'width: 300px;', 'class': 'form-control'}))
    Location = forms.CharField(label='Restaurant Location', max_length=100, widget=forms.TextInput(attrs={'placeholder': 'Location', 'style': 'width: 300px;', 'class': 'form-control'}))
    URL = forms.CharField(label='Menu URL', max_length=100, widget=forms.TextInput(attrs={'placeholder': 'URL', 'style': 'width: 300px;', 'class': 'form-control'}))
    priceOPTIONS= ((("£", "£"), ("££", "££"), ("£££", "£££") ))
    Price = forms.MultipleChoiceField(widget=forms.CheckboxSelectMultiple,choices=priceOPTIONS)
    Rating = forms.IntegerField(widget=forms.TextInput(attrs={'placeholder': 'Rating', 'style': 'width: 300px;', 'class': 'form-control'}))
    Cuisine = forms.CharField(label='Restaurant Cuisine(s)', max_length=100, widget=forms.TextInput(attrs={'placeholder': 'Separate multiple by space', 'style': 'width: 300px;', 'class': 'form-control'}))
    Image = forms.ImageField(required=False)
