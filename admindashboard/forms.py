from django import forms
from core.models import Customers,Product,Category,CategoryofCategories


class Customers_forms(forms.ModelForm):
    
    class Meta:
        model = Customers
        fields = '__all__'
        widgets = {
            'Name': forms.TextInput(attrs={'class': 'textinput'}),
            'Username': forms.TextInput(attrs={'class': 'textinput'}),
            'Email': forms.EmailInput(attrs={'class': 'textinput'}),
            'password': forms.PasswordInput(attrs={'class': 'textinput'}),
            'is_staff': forms.CheckboxInput(),
            'is_superuser': forms.CheckboxInput(),
        }


class Products_forms(forms.ModelForm):
    category = forms.ModelChoiceField(queryset=Category.objects.all(), widget=forms.Select(attrs={'class': 'form-select'}))
    product_categoryofcategories = forms.ModelChoiceField(queryset=CategoryofCategories.objects.none(), widget=forms.Select(attrs={'class': 'form-select'}))
        
    class Meta:
        model = Product
        fields = '__all__'
        widgets = {
            'product_name': forms.TextInput(attrs={'class': 'textinput'}),
            'product_info': forms.Textarea(attrs={'class': 'textinput'}),
            'product_price': forms.TextInput(attrs={'class': 'textinput'}),
            'product_image': forms.ClearableFileInput(attrs={'class': 'textinput'}),
            'product_stock': forms.NumberInput(attrs={'class': 'textinput'}),
        }
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        if self.is_bound and 'category' in self.data:
            v=self.data.get('category')
            self.fields['product_categoryofcategories'].queryset=CategoryofCategories.objects.filter(categoryfrom=v)




      