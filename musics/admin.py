from django import forms
from django.contrib import admin
from django.db import models

from musics.api_music import Music


@admin.register(Music)
class MusicAdmin(admin.ModelAdmin):
    formfield_overrides = {
        models.CharField: {
            "widget": forms.TextInput(attrs={"style": "width: 500px; height: 50px;"})
        },
    }
