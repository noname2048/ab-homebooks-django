from django import forms
from django.core.validators import EmailValidator
from django.contrib.auth import forms as auth_forms, get_user
from django.contrib.auth import get_user_model

class AccountEmailForm(forms.Form):
    email = forms.EmailField(help_text="user_email", validators=[EmailValidator()])

class AccountSignupForm(auth_forms.UserCreationForm):

    class Meta(auth_forms.UserChangeForm.Meta):
        model = get_user_model()
        fields = ("email", )

class NoPasswordSignupForm(forms.Form):

    class Meta:
        model = get_user_model()
        fields = ["email", "name"]

        