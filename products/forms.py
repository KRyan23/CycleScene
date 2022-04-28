''' Required Imports '''
from django import forms
from .models import Product, Category

class ProductForm(forms.ModelForm):
    ''' Product Form Class '''
    class Meta:
        model = Product
        fields = '__all__'

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        categories = Category.objects.all()
        my_friendly_name = [(cat.id, cat.get_friendly_name()) for cat in categories]

        self.fields['category'].choices = my_friendly_name
        for field_name, field in self.fields.items():
            field.widget.attrs['class'] = 'stripe-style-input'
