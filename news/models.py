from django.db import models

# Create your models here.

from ckeditor_uploader.fields import  RichTextUploadingField

class News(models.Model):
    title = models.CharField(max_length=50)
    content = RichTextUploadingField()
    created = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.title

