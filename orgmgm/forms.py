from django import forms

from .models import Kontakt, Organisation, Bundesland, Activity
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User

# Froms to add records

class AddKontaktForm (forms.ModelForm):
    class Meta:
        model = Kontakt
        exclude = ()


class AddOrganisationForm (forms.ModelForm):
    class Meta:
        model = Organisation
        exclude = ()

class AddActivityForm(forms.ModelForm):
    class Meta:
        model = Activity
        exclude = ()


# Forms to search data

class SearchKontaktForm(forms.Form):
    nachname = forms.CharField(label='Nachname', required=False)
    vorname = forms.CharField(label='Vorname', required=False)
    organisation = forms.CharField(label='Organisation Name', required=False)


class SearchOrganisationForm (forms.Form):
    orgname = forms.CharField(label='Organisation Name', required=False)
    plz = forms.CharField(label='Postleitzahl', required=False)
    stadt = forms.CharField(label='Stadt', required=False)
    bundesland = forms.CharField(label='Bundesland', required=False)


# Form to Sign Up 

class SignUpForm(UserCreationForm):
    first_name = forms.CharField(max_length=30, required=True, help_text='Required.')
    last_name = forms.CharField(max_length=30, required=True, help_text='Required.')
    email = forms.EmailField(max_length=254, help_text='Required. Input a valid email address.')

    class Meta:
        model = User
        fields = ('username', 'first_name', 'last_name', 'email', 'password1', 'password2', )