from django import forms

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
