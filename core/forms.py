from django import forms
from .models import Customers


class Customers_forms(forms.ModelForm):
    class Meta:
        model=Customers
        fields=[
            'Name','Username','Email','password'
        ]