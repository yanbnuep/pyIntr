from django.db import models

# Create your models here.
from ckeditor.fields import RichTextField

from django import forms
from django.contrib import admin
from ckeditor.widgets import CKEditorWidget


class Post(models.Model):
    content = RichTextField()


class PostAdminForm(forms.ModelForm):
    content = forms.CharField(widget=CKEditorWidget())

    class Meta:
        model = Post


class PostAdmin(admin.ModelAdmin):
    form = PostAdminForm


admin.site.register(Post, PostAdmin)
