from tkinter import Widget
from unicodedata import name
from django import forms
from .models import customer


class CustomerRegisteration(forms.ModelForm):
    password = forms.CharField(max_length=72, widget=forms.PasswordInput
                               (render_value=True))  # custom widget is set for password field.

    class Meta:
        model = customer
        fields = ['name', 'email', 'password','image']

        Widget = {
            'name': forms.TextInput(attrs={'class': 'form-control'}),
            'email': forms.EmailInput(attrs={'class': 'form-control'}),
            'password': forms.PasswordInput(render_value=True, attrs={'class': 'form-control'}),
            'image': forms.ImageField(),
        }
