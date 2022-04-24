''' Required imports '''
from django import forms
from .models import Order

class OrderForm(forms.ModelForm):
    ''' Orderform class '''
    class Meta:
        model = Order
        fields = ('first_name', 'last_name', 'email',
                  'mobile_number', 'address1',
                  'address2', 'county', 'city',
                  'country','postcode', )
# Mostly from BA project
    def __init__(self, *args, **kwargs):
        ''' Place holders for fields to overwrite the default labels and 
        set autofocus on first_name '''
        super().__init__(*args, **kwargs)

        placeholders = {
            'first_name': 'First Name',
            'last_name': 'Last Name',
            'email': 'Email Address',
            'mobile_number': 'Mobile Phone',
            'address1': 'Address Line 1',
            'address2': 'Address Line 2',
            'county': 'County',
            'city': 'City',
            'postcode': 'Postcode',
        }

        self.fields['first_name'].widget.attrs['autofocus'] = True
        for field in self.fields:
            if field != 'country':
                if self.fields[field].required:
                    placeholder = f'{placeholders[field]} *'
                else:
                    placeholder = placeholders[field]
                self.fields[field].widget.attrs['placeholder'] = placeholder
            self.fields[field].widget.attrs['class'] = 'stripe-style-input'
            self.fields[field].label = False
