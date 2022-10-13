import numbers
from django import forms

class ContactForm(forms.Form):
    name = forms.CharField(max_length=255)
    address = forms.CharField(max_length=255)
    email = forms.EmailField()
    phonenumber = forms.CharField(max_length=255)