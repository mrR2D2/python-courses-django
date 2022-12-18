
from django.contrib.auth import views as auth_views
from django.urls import path, reverse_lazy

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


urlpatterns_materials = [  # /materials/
    path("<slug:slug>", view=views.material, name="fetch-one-material"),
    path("<slug:slug>/share", view=views.share_material, name="share-material"),
]


urlpatterns_auth = [
    path("register/", view=views.register, name="register"),
    path("login/", view=auth_views.LoginView.as_view(), name="login"),
    path("logout/", view=auth_views.LogoutView.as_view(), name="logout"),
    
    path(
        "password_reset/", 
        view=auth_views.PasswordResetView.as_view(),
        name="password_reset",
    ),
    path(
        "password_reset/done",
        view=auth_views.PasswordResetDoneView.as_view(),
        name="password_reset_done",
    ),
    path(
        "reset/<uidb64>/<token>/",
        view=auth_views.PasswordResetConfirmView.as_view(),
        name="password_reset_confirm"
    ),
    path(
        "reset/done",
        view=auth_views.PasswordResetCompleteView.as_view(),
        name="password_reset_complete",
    ),
]