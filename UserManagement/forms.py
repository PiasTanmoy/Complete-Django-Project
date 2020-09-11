from django import forms
from .models import Profile

class ProfileForm(forms.ModelForm):
    class Meta:
        model=Profile
        fields = ('contact_no', 'mobile_no', 'pro_pic', 'portfolio_url', 'cv')