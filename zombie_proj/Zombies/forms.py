from django import forms
from django.contrib.auth.models import User
from Zombies.models import Player

class UserForm(forms.ModelForm):
    password = forms.CharField(widget=forms.PasswordInput())

    class Meta:
        model = User
        fields = ('username', 'email', 'password')

class PlayerForm(forms.ModelForm):

    class Meta:
        model = Player
        fields = ('badge1_display', 'badge2_display', 'badge3_display', 'badge4_display',)

class AddForm(forms.ModelForm):

    class Meta:
        model = Player
        fields = ('friends',)

class SearchForm(forms.Form):
    search =  forms.CharField(label='Search for new users', max_length=100)

