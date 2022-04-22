from django import forms
from .models import *
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm


class CreateUserForm(UserCreationForm):
    class Meta:
        model = User
        fields = '__all__'


class ContactForme(forms.ModelForm):
    class Meta:
        model = Contact
        fields = '__all__'


class ProductForme(forms.ModelForm):
    class Meta:
        model = Product
        fields = '__all__'


class CrocekryForme(forms.ModelForm):
    class Meta:
        model = Crocekry
        fields = '__all__'

