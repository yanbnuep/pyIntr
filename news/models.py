from django.db import models


# Create your models here.
from ckeditor_uploader.fields import  RichTextUploadingField
from django_resized import ResizedImageField

class News(models.Model):
    title = models.CharField(max_length=50)
    cover = ResizedImageField(upload_to='coverImg/', size=[500, 300])
    content = RichTextUploadingField(blank=True, null=True, verbose_name="context")
    created = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.title

