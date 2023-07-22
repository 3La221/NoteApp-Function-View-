from django.forms import ModelForm
from django import forms
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm
from .models import Note


class NoteForm(forms.ModelForm):
	class Meta:
		model = Note
		fields = ['title','desc','complete']


class RegisterForm(UserCreationForm):
	class Meta:
		model = User
		fields =['username','password1','password2'] 
		