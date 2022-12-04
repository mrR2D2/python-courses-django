from django.contrib import admin

from . import models


@admin.register(models.LessonEntity)
class LessonEntityAdmin(admin.ModelAdmin):
    """
    Admin model for LessonEntity.
    """
    list_display = ("title", "slug")
    ordering = ("slug", )


@admin.register(models.MaterialEntity)
class MaterialEntityAdmin(admin.ModelAdmin):
    """
    Admin model for MaterialEntity.
    """
    list_display = ("title", "slug", "material_type")
    ordering = ("slug", )


@admin.register(models.CommentEntity)
class CommentEntityAdmin(admin.ModelAdmin):
    list_display = ("lesson", "body", "created_by", "created_at", "updated_at")
    ordering = ("lesson", "created_at")


@admin.register(models.ProfileEntity)
class ProfileEntityAdmin(admin.ModelAdmin):
    """
    Admin model for ProfileEntity.
    """
    list_display = ("avatar", "user", "birthday")
