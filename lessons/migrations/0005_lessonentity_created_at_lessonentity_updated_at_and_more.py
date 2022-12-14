# Generated by Django 4.1.3 on 2022-12-02 17:55

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('lessons', '0004_alter_profileentity_avatar_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='lessonentity',
            name='created_at',
            field=models.DateTimeField(auto_now_add=True, null=True),
        ),
        migrations.AddField(
            model_name='lessonentity',
            name='updated_at',
            field=models.DateTimeField(auto_now=True, null=True),
        ),
        migrations.AddField(
            model_name='materialentity',
            name='created_at',
            field=models.DateTimeField(auto_now_add=True, null=True),
        ),
        migrations.AddField(
            model_name='materialentity',
            name='updated_at',
            field=models.DateTimeField(auto_now=True, null=True),
        ),
    ]
