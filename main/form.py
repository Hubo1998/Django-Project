from unittest.util import _MAX_LENGTH
from django import forms


class CreateNewList(forms.Form):
    name=forms.CharField(label="Name",max_length=200)
    check=forms.BooleanField(required=False)
