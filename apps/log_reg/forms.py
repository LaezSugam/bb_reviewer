from django.forms import ModelForm
from django import forms
from django.utils.translation import ugettext_lazy as _
from django.core.validators import MinLengthValidator
from models import User

class UserForm(ModelForm):
	confirm_password = forms.CharField(widget = forms.PasswordInput(), validators=[MinLengthValidator(8, "Password must be at least 8 characters.")])
	class Meta:
		model = User
		fields = ["name", "username", "email", "pw_hash"]
		labels = {
			"name": _("Name"),
			"username": _("Alias"),
			"email": _("Email Address"),
			"pw_hash": _("Password"),
		}
		widget = {
			"pw_hash": forms.PasswordInput()
		}

	def clean(self):
		cleaned_data = super(UserForm, self).clean()
		password = cleaned_data.get("pw_hash")
		confirm_password = cleaned_data.get("confirm_password")

		if password != confirm_password:
			raise forms.ValidationError( "password and confirm password do not match")
