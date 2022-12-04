from django.shortcuts import redirect, render, get_object_or_404
from django.http import HttpResponse

from . import forms
from . import models


def all_lessons(request):
    lessons = models.LessonEntity.objects.all()
    return render(request, "lessons/lessons.html", {"lessons": lessons})


def lesson(request, slug):    
    lesson = get_object_or_404(models.LessonEntity, slug=slug)
    return render(request, "lessons/lesson.html", {"lesson": lesson})


def edit_lesson(request, slug):
    lesson = get_object_or_404(models.LessonEntity, slug=slug)
    if request.method == "POST":
        lesson_form = forms.LessonForm(request.POST, instance=lesson)
        if lesson_form.is_valid():
            lesson_form.save()
        return render(
            request,
            "lessons/lesson.html",
            {"lesson": lesson},
        )
    else:
        lesson_form = forms.LessonForm(instance=lesson)
        return render(
            request,
            "lessons/edit.html",
            {
                "form": lesson_form,
                "lesson": lesson,
            },
        )



def material(request, slug):
    material = get_object_or_404(models.MaterialEntity, slug=slug)
    return render(request, "materials/material.html", {"material": material})


def create_material(request, lesson_slug):
    lesson = get_object_or_404(models.LessonEntity, slug=lesson_slug)
    if request.method == "POST":
        material_form = forms.MaterialForm(request.POST)
        if material_form.is_valid():
            new_material = material_form.save()
            new_material.slug = f"MATERIAL-{new_material.id}"
            new_material.lessons.add(lesson)
            new_material.save()
            return render(
                request, 
                "lessons/lesson.html", 
                {"lesson": lesson},
            )

    return render(
        request, 
        "materials/create.html", 
        {"form": forms.MaterialForm}
    )


def register(request):
    if request.method == "POST":
        registration_form = forms.RegistrationForm(request.POST)
        if registration_form.is_valid():
            new_user = registration_form.save(commit=False)
            new_user.set_password(registration_form.cleaned_data["password"])
            new_user.save()
            models.ProfileEntity.objects.create(user=new_user)
            return render(
                request,
                "registration/registration_complete.html",
                {"new_user": new_user},
            )
        else:
            return HttpResponse("Bad credentials")

    registration_form = forms.RegistrationForm()
    return render(
        request,
        "registration/register.html",
        {"form": registration_form},
    )
