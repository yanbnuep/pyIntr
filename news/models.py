from django.db import models

# Create your models here.
from ckeditor.fields import RichTextField

from django import forms
from django.contrib import admin
from ckeditor.widgets import CKEditorWidget


class Post(models.Model):
    content = RichTextField()



admin.site.register(Post)
