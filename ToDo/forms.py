from cProfile import label
from dataclasses import field, fields
from pyexpat import model
from .models import challenge_list_Model
from django import forms


class challege_list_Form(forms.ModelForm):
    class Meta:
        model = challenge_list_Model
        fields = "__all__"
