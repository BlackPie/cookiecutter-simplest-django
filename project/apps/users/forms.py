from django import forms
from django.utils.translation import ugettext_lazy as _


class SignupForm(forms.Form):
    username = forms.CharField(label=_("Username"), max_length=30)
    first_name = forms.CharField(label=_("First name"))
    last_name = forms.CharField(label=_("Last name"))
    password1 = forms.CharField(label=_("Password"), max_length=30, widget=forms.PasswordInput())
    password2 = forms.CharField(label=_("Password again"), max_length=30, widget=forms.PasswordInput())
    email = forms.EmailField(label=_("Email"), required=False)

    def clean(self):
        if 'password1' in self.cleaned_data and 'password2' in self.cleaned_data:
            if self.cleaned_data['password1'] != self.cleaned_data['password2']:
                raise forms.ValidationError("passwords dont match each other")
        return self.cleaned_data
