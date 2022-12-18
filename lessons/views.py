from django.contrib.auth.decorators import login_required
from django.shortcuts import redirect, render, get_object_or_404
from django.http import HttpResponse
from django.core.mail import send_mail

from . import forms
from . import models


@login_required
def all_lessons(request):
    lessons = models.LessonEntity.objects.all()
    return render(
        request, 
        "lessons/lessons.html", 
        {
            "lessons": lessons,
        })


@login_required
def lesson(request, slug):    
    lesson = get_object_or_404(models.LessonEntity, slug=slug)
    return render(request, "lessons/lesson.html", {"lesson": lesson})


@login_required
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


@login_required
def material(request, slug):
    material = get_object_or_404(models.MaterialEntity, slug=slug)
    return render(request, "materials/material.html", {"material": material})


@login_required
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
        else:
            render(
                request, 
                "materials/create.html", 
                {
                    "material_types": models.MaterialEntity.MATERIAL_TYPES,
                    "title_error": material_form.errors["title"][0],
                    "body_error": material_form.errors["body"][0],
                }  
            )

    return render(
        request, 
        "materials/create.html", 
        {
            "material_types": models.MaterialEntity.MATERIAL_TYPES,
        }
    )


def _prepare_email(material, cd, request):
    uri = request.build_absolute_uri(material.get_absolete_url())
    body = (
        f"<a href='{uri}'>{material.title}</a> was recommended to you by {cd['my_name']}.\n\n"
        f"Comment: {cd['comment']}"
    )
    subject = f"{cd['my_name']} recommends you {material.title}"
    return subject, body


def share_material(request, slug):
    material = get_object_or_404(models.MaterialEntity, slug=slug)
    is_sent = False
    if request.method == "POST":
        form = forms.EmailMaterialForm(request.POST)
        if form.is_valid():
            cd = form.cleaned_data
            subject, body = _prepare_email(material, cd, request)
            send_mail(subject, body, "admin@admin.com", [cd["to_email"]])
            is_sent = True
    else:
        form = forms.EmailMaterialForm()
    return render(
        request,
        "materials/share.html",
        {
            "form": form,
            "material": material,
            "is_sent": is_sent,
        }
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
