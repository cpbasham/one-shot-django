from django import forms
from django.contrib.auth.models import User


class LoginForm(forms.ModelForm):
	class Meta:
		model = User
		fields = ['username', 'password']
		widgets = {'password': forms.PasswordInput()}
		help_texts = {'username': ""}

class RegisterForm(forms.ModelForm):
	password_confirmation = forms.CharField(label="Confirmation", widget=forms.PasswordInput)
	class Meta:
		model = User
		fields = ['username', 'password']
		widgets = {'password': forms.PasswordInput()}
		help_texts = {'username': ""}
		#labels = {'username': 'username'}
		# error_messages = {}
	def clean_password_confirmation(self):
		conf = self.cleaned_data['password_confirmation']
		if conf != self.cleaned_data['password']:
			raise forms.ValidationError("passwords must match")




# class LoginForm(forms.Form):
# 	username = forms.CharField(label="Username", max_length=32)
# 	password = forms.CharField(label="Password", widget=forms.PasswordInput)

# 	def clean_password(self):
# 		data = self.cleaned_data['password']
# 		if

# class RegisterForm(LoginForm):
# 	password_confirmation = forms.CharField(label="Confirmation", widget=forms.PasswordInput)