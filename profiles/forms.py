''' Required Imports '''
from django import forms
from .models import UserProfile

class UserProfileForm(forms.ModelForm):
    ''' User Profile Form '''
    class Meta:
        model = UserProfile
        exclude = ('user', )
    # Mostly from BA project
    def __init__(self, *args, **kwargs):
        ''' Place holders for fields to overwrite the default labels and
        set autofocus on first_name '''
        super().__init__(*args, **kwargs)

        placeholders = {
            'default_mobile_phone': 'Mobile Phone',
            'default_address1': 'Address Line 1',
            'default_address2': 'Address Line 2',
            'default_county': 'County',
            'default_city': 'City',
            'default_postcode': 'Postcode',
        }

        self.fields['default_mobile_phone'].widget.attrs['autofocus'] = True
        for field in self.fields:
            if field != 'default_country':
                if self.fields[field].required:
                    placeholder = f'{placeholders[field]} *'
                else:
                    placeholder = placeholders[field]
                self.fields[field].widget.attrs['placeholder'] = placeholder
            self.fields[field].widget.attrs['class'] = 'stripe-style-input'
            self.fields[field].label = False
