from dataclasses import fields
from pyexpat import model
from django.forms import ModelForm
from .models import Room, User
from django.contrib.auth.forms import UserCreationForm

class MyUserCreationForm(UserCreationForm):
    class Meta:
        model = User
        fields = ['name','username','email', 'password1', 'password2']

class roomForm(ModelForm):
    class Meta:
        model = Room
        fields = '__all__' #['name', 'body']
        exclude = ['host', 'participants']

class userForm(ModelForm):
    class Meta:
        model = User
        fields = ['name','username', 'email','bio','avatar']