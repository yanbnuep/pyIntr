from django.db import models

# Create your models here.
from ckeditor.fields import RichTextField

from django import forms
from django.contrib import admin
from ckeditor.widgets import CKEditorWidget


class News(models.Model):
    title = models.CharField(max_length=50)
    content = RichTextField()
    created = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.News_text

