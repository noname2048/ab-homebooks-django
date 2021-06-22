from django import forms
from django.core.validators import EmailValidator
from django.contrib.auth import forms as auth_forms, get_user
from django.contrib.auth import get_user_model
from django.contrib.auth.forms import UserCreationForm
from django.forms import widgets
from django.contrib.auth import password_validation
from django.core.exceptions import ValidationError

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


from logging import getLogger

logger = getLogger(__name__)


class SignupForm(forms.Form):
    """fbv + form, formview + form"""

    email = forms.EmailField(required=True)
    name = forms.CharField(required=True)
    password1 = forms.CharField(required=True, widget=forms.PasswordInput(), strip=False)
    password2 = forms.CharField(required=True, widget=forms.PasswordInput(), strip=False)

    error_messages = {"password_mismatch": "The two password fields didn't match"}

    def clean_password1(self):
        password1 = self.cleaned_data.get("password1")
        if password1:
            try:
                password_validation.validate_password(password1)
            except ValidationError as error:
                self.add_error("password1", error)

    def clean_password2(self):
        logger.debug("hi")
        password1 = self.cleaned_data.get("password1")  # 작동하지 않음
        password2 = self.cleaned_data.get("password2")

        if password1 and password2 and password1 != password2:
            raise ValidationError(
                self.error_messages["password_mismatch"], code="password_mismatch"
            )
        return password2


class SignupModelForm(forms.ModelForm):
    password1 = forms.CharField(required=True, widget=widgets.PasswordInput)
    password2 = forms.CharField(required=True, widget=widgets.PasswordInput)

    class Meta:
        model = UserModel
        fields = (
            "email",
            "name",
        )

    def __init__(self, *args, **kwargs):
        super().__init__(*args, *kwargs)
        if self._meta.model.USERNAME_FIELD in self.fields:
            self.fields[self._meta.model.USERNAME_FIELD].widget.attrs["autofocus"] = True

    def clean_password2(self):
        password1 = self.cleaned_data.get("password1")
        password2 = self.cleaned_data.get("password2")

        if password1 and password2 and password1 != password2:
            raise ValidationError(
                self.error_messages["password_mismatch"], code="password_mismatch"
            )
        return password2

    def _post_clean(self):
        super()._post_clean()
        password = self.cleaned_data.get("password2")
        if password:
            try:
                password_validation.validate_password(password, self.instance)
            except ValidationError as error:
                self.add_error("password2", error)

    def save(self, commit=True):
        user = super().save(commit=False)
        user.set_password(self.cleaned_data["password1"])
        if commit:
            user.save()
        return user
