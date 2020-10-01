from django import forms
from .models import Profile, Chat

class ProfileForm(forms.ModelForm):
    class Meta:
        model=Profile
        fields = ('contact_no', 'mobile_no', 'pro_pic', 'portfolio_url', 'cv')

class ChatForm(forms.ModelForm):
    class Meta:
        model = Chat
        fields = ('receiver', 'message','image' ,'file')
