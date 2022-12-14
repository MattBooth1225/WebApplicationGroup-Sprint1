from django import forms
from store.models import Profile

class OrderCreateForm(forms.ModelForm):
    class Meta:
        model = Profile
        fields = ['profile_fname', 'profile_lname', 'profile_email', 'profile_addressMain',
                  'profile_zipcode', 'profile_city', 'profile_cardnum', 'profile_exp_date', 'profile_sec_code']
        labels = {
            'profile_fname': 'First Name',
            'profile_lname': 'Last Name',
            'profile_email': 'Email Address',
            'profile_addressMain': 'Address',
            'profile_zipcode': 'Zip Code',
            'profile_city': 'City',
            'profile_cardnum': 'Card Number',
            'profile_exp_date': 'Expiration Date',
            'profile_sec_code': 'Security Code'
        }


