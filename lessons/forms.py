from django import forms
from django.contrib.auth.models import User

from . import models


class MaterialForm(forms.ModelForm):
    class Meta:
        model = models.MaterialEntity
        fields = (
            "title", 
            "body", 
            "material_type",
        )


class LessonForm(forms.ModelForm):
    class Meta:
        model = models.LessonEntity
        fields = (
            "title",
            "description",
        )


class RegistrationForm(forms.ModelForm):

    password = forms.CharField(
        label="password",
        widget=forms.PasswordInput,
    )

    password2 = forms.CharField(
        label="repeat password",
        widget=forms.PasswordInput,
    )

    class Meta:
        model = User
        fields = (
            "username", 
            "first_name", 
            "email",
        )

    def clean_password2(self):
        cd = self.cleaned_data
        if cd["password"] != cd["password2"]:
            raise forms.ValidationError("Passwords are not equal")
        return cd["password2"]
