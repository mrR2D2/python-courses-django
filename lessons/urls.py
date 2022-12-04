
from django.urls import path

from . import views

urlpatterns_lessons = [
    path("", view=views.all_lessons, name="fetch-all-lessons"),
    path("<slug:slug>/", view=views.lesson, name="fetch-one-lesson"),
    path("<slug:slug>/edit", view=views.edit_lesson, name="edit-lesson"),
    path(
        "<slug:lesson_slug>/materials",  # lessons/<slug>/materials
        view=views.create_material, 
        name="create-material",
    ),
]


urlpatterns_materials = [
    path("<slug:slug>", view=views.material, name="fetch-one-material"),
]
