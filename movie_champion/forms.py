from django import forms
from .models import Movie, Customer
from django.contrib.auth.models import User


class MovieForm(forms.ModelForm):
    class Meta:
        model = Movie
        fields = ('movie_name', 'movie_genre', 'staring', 'director', 'rating', 'price')


class CustomerForm(forms.ModelForm):
    class Meta:
        model = Customer
        fields = ('cust_name', 'account_number', 'address',
                  'city', 'state', 'zipcode', 'email', 'phone_number')


class UserRegistrationForm(forms.ModelForm):
    password = forms.CharField(label='Password', widget=forms.PasswordInput)
    password2 = forms.CharField(label='Repeat password', widget=forms.PasswordInput)
    class Meta:
        model = User
        fields = ('username', 'first_name', 'email')
    def clean_password2(self):
        cd = self.cleaned_data
        if cd['password'] != cd['password2']:
            raise forms.ValidationError('Passwords don\'t match.')
        return cd['password2']