from django.db import models
from django.conf import settings
from django.urls import reverse


class WithTimeTracking(models.Model):

    created_at = models.DateTimeField(auto_now_add=True, null=True)
    updated_at = models.DateTimeField(auto_now=True, null=True)
    class Meta:
        abstract = True


class MaterialEntity(
    WithTimeTracking,
    models.Model
):
    """
    Model for Materials entity.
    """

    THEORY_MATERIAL = 'theory'
    PRACTICE_MATERIAL = 'practice'
    TEST_MATERIAL = 'test'
    MATERIAL_TYPES = (
        (THEORY_MATERIAL, 'Theoretic Materials'), 
        (PRACTICE_MATERIAL, 'Practical Material'),
        (TEST_MATERIAL, 'Testing Material'),
    )

    title = models.CharField(max_length=64)
    slug = models.SlugField(max_length=8)
    body = models.TextField()
    material_type = models.CharField(
        max_length=16, 
        choices=MATERIAL_TYPES,
        default=THEORY_MATERIAL,
    )

    def __str__(self) -> str:
        return self.slug
    
    def get_absolete_url(self) -> str:
        return reverse("fetch-one-material", args=[self.slug])


class LessonEntity(
    WithTimeTracking,
    models.Model,
):
    """
    Model for Lesson entity.
    """

    title = models.CharField(max_length=64)
    slug = models.SlugField(max_length=8)
    description = models.TextField()

    materials = models.ManyToManyField(
        MaterialEntity, 
        related_name="lessons",
    )

    def __str__(self) -> str:
        return self.slug

    def get_absolete_url(self) -> str:
        return reverse("fetch-one-lesson", args=[self.slug])


class CommentEntity(
    WithTimeTracking,
    models.Model,
):
    lesson = models.ForeignKey(
        LessonEntity,
        on_delete=models.CASCADE,
        related_name="comments",
    )

    body = models.TextField()
    created_by = models.ForeignKey(
        settings.AUTH_USER_MODEL,
        on_delete=models.SET_NULL,
        related_name="user_comments",
        null=True,
    )

    def __str__(self) -> str:
        return f"COMMENT <{self.body}>"


class ProfileEntity(models.Model):
    """
    Model for Profile entity.
    """

    birthday = models.DateField(null=True, blank=True)
    avatar = models.ImageField(upload_to="avatars", null=True, blank=True)
    user = models.OneToOneField(
        settings.AUTH_USER_MODEL,
        on_delete=models.CASCADE,
    )

    def __str__(self) -> str:
        return self.user
