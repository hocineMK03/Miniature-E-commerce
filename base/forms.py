from django import forms
from core.models import Customers


class Customers_forms1(forms.ModelForm):
    class Meta:
        model=Customers
        fields=[
            'Email','password'
        ]