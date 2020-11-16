from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.core.exceptions import ValidationError
from .models import Writer


class WriterCreationForm(forms.ModelForm):

    password1 = forms.CharField(label='Password', widget=forms.PasswordInput)
    password2 = forms.CharField(label='Password repeat', widget=forms.PasswordInput)

    class Meta:
        model = Writer
        fields = ['email', 'first_name', 'last_name', 'web_site', 'signing']

    def clean_password2(self):
        password1 = self.cleaned_data.get("password1")
        password2 = self.cleaned_data.get('password2')
        if password1 and password2 and password1 != password2:
            raise ValidationError("Passwords don't match")
        return password2

    def save(self, commit=True):
        writer = super().save(commit=False)
        writer.set_password(self.cleaned_data["password1"])
        if commit:
            writer.save()
        print("USUARIO: ", writer, " GUARDADO CON EXITO")
        return writer


class WriterLoginForm(forms.ModelForm):

    password = forms.CharField(label="Password", widget=forms.PasswordInput)

    class Meta:
        model = Writer
        fields = ['email']