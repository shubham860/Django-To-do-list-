from django import forms
from todo.models import List

class ListForm(forms.ModelForm):
    class Meta:
        model = List
        fields = ("item","completed")
