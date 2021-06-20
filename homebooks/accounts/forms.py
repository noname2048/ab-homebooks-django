from django import forms
from django.core.validators import EmailValidator
from django.contrib.auth import forms as auth_forms, get_user
from django.contrib.auth import get_user_model
from django.contrib.auth.forms import UserCreationForm

UserModel = get_user_model()


class AccountEmailForm(forms.Form):
    email = forms.EmailField(help_text="user_email", validators=[EmailValidator()])


class AccountSignupForm(auth_forms.UserCreationForm):
    class Meta(auth_forms.UserChangeForm.Meta):
        model = get_user_model()
        fields = ("email",)


class NoPasswordSignupForm(UserCreationForm):
    class Meta(UserCreationForm.Meta):
        model = UserModel
        fields = (
            "email",
            "name",
        )


from django.core.exceptions import ValidationError


class DjangoCustomSignupForm(forms.Form):

    email = forms.EmailField(required=True)
    name = forms.CharField(required=True)
    password1 = forms.CharField(widget=forms.PasswordInput(), strip=False)
    password2 = forms.CharField(widget=forms.PasswordInput(), strip=False)

    error_messages = {"password_mismatch": "The two password fields didn't match"}

    def clean_password2(self):
        password1 = self.cleaned_data.get("password1")
        password2 = self.cleaned_data.get("password2")
        if password1 and password2 and password1 != password2:
            raise ValidationError(
                self.error_messages["password_mismatch"], code="password_mismatch"
            )
        return password2
