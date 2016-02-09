from django import forms
from django.utils.translation import ugettext_lazy as _

from crispy_forms.helper import FormHelper
from crispy_forms.layout import Submit, Layout
from crispy_forms.bootstrap import FormActions


class SignupForm(forms.Form):
    username = forms.CharField(label=_("Username"), max_length=30)
    first_name = forms.CharField(label=_("First name"))
    last_name = forms.CharField(label=_("Last name"))
    password1 = forms.CharField(label=_("Password"), max_length=30, widget=forms.PasswordInput())
    password2 = forms.CharField(label=_("Password again"), max_length=30, widget=forms.PasswordInput())
    email = forms.EmailField(label=_("Email"), required=False)

    helper = FormHelper()
    helper.form_method = 'POST'
    helper.layout = Layout(
        'first_name',
        'username',
        'last_name',
        'password1',
        'password2',
        'email',
        FormActions(Submit('signup', 'join', css_class='btn-primary form-button'))
    )
