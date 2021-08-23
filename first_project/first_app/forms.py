from django import forms
from first_app.models import Users, UserProfileInfo
from django.contrib.auth.models import User


class FormClass(forms.Form):
    name = forms.CharField()
    email = forms.EmailField()
    reverifyemail = forms.EmailField()
    address = forms.CharField(widget=forms.Textarea())
    botcacher = forms.CharField(required=False,widget=forms.HiddenInput)

    def clean(self):
        cleaned_data = super().clean()
        email = cleaned_data.get('email')
        reverifyemail = cleaned_data.get('reverifyemail')

        if email != reverifyemail:
            raise forms.ValidationError("Emails should match")

class Users_form(forms.ModelForm):
    class Meta:
        model = Users
        fields = "__all__"


class UserForm(forms.ModelForm):
    password = forms.CharField(widget=forms.PasswordInput())

    class Meta:
        model = User
        fields = ['username','email','password']

class UserProfileInfoForm(forms.ModelForm):

    class Meta:
        model = UserProfileInfo
        fields = ['portfolio_url','profile_picture']
