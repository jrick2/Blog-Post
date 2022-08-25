from django import forms
from django.contrib.auth.forms import UserCreationForm, UserChangeForm
from django.contrib.auth.models import User
from django.views import generic
from django.urls import reverse_lazy

class NewUserForm(UserCreationForm):
	email = forms.EmailField(required=True)

	class Meta:
		model = User
		fields = ("email", "username", "password1", "password2")

	def save(self, commit=True):
		user = super(NewUserForm, self).save(commit=False)
		user.email = self.cleaned_data['email']
		if commit:
			user.save()

		return user

class UserEditView(generic.CreateView):
	form_class = UserChangeForm
	template_name = 'profile.html'
	success_url = reverse_lazy('home')