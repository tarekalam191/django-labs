from django import forms
from author.models import Author
from .models import *

class Addbook (forms.Form):
    title=forms.CharField(required=True,max_length=200)
    vergion=forms.NumberInput()
    author=forms.ChoiceField(choices=Author.get_all_author)


class AddBookModel(forms.ModelForm):
    class Meta:
        model=Book
        fields='__all__'