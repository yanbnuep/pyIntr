from django.db import models

# Create your models here.
from django import forms
from django.contrib import admin
from ckeditor_uploader.widgets import CKEditorUploadingWidget

class News(models.Model):
    title = models.CharField(max_length=50)
    content =  forms.CharField(widget=CKEditorUploadingWidget())
    created = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.title

