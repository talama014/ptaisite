from django import forms
from django.forms import ModelForm, fields, models
from .models import Room

class RoomForm(ModelForm):
    class Meta:
        model = Room
        fields = '__all__'
    