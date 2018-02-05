from django import forms
from django.core import validators
from django.contrib.auth.models import User
from .models import UserProfileInfo

class UserForm(forms.ModelForm):
    password = forms.CharField(widget=forms.PasswordInput())

    class Meta():
        model = User
        fields = ('username','email','password')

class UserProfileInfoForm(forms.ModelForm):
    class Meta():
        model = UserProfileInfo
        fields = ('portofolio_site','profile_pic')

class form1(forms.Form):
    name = forms.CharField(max_length=100)
    email = forms.EmailField()
    verifyemail = forms.EmailField(label='enter your email again')
    text = forms.CharField(widget=forms.Textarea)

    def clean(self):
        all_clean_data = super().clean()
        email = all_clean_data['email']
        vemail = all_clean_data['verifyemail']

        if email != vemail:
            raise forms.ValidationError('make sure you your email match!')

class form2(forms.Form):
    name = forms.CharField(max_length=100)
