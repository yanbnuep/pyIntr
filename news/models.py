from django.db import models

# Create your models here.
from ckeditor_uploader.fields import  RichTextUploadingField

class coverImg(models.Model):
    cover = models.ImageField(upload_to='media/coverImg', blank=True, null=True)
    def image_thumb(self):
        return '<img src="media/%s" width="100" height="100" />' % (self.cover)
    image_thumb.short_description = 'Image'
    image_thumb.allow_tags = True

class News(models.Model):
    title = models.CharField(max_length=50)

    content = RichTextUploadingField(blank=True,null=True,verbose_name="context")
    created = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.title

