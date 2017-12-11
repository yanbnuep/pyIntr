from django.db import models

# Create your models here.
from ckeditor_uploader.fields import  RichTextUploadingField

class News(models.Model):
    title = models.CharField(max_length=50)
    cover = models.ImageField(upload_to='static/media/coverImg', blank=True, null=True)
    def image_thumb(self):
        return '<img src="/media/coverImg/%s" width="100" height="100" />' % (self.cover)
        image_thumb.allow_tags = True
    content = RichTextUploadingField(blank=True,null=True,verbose_name="context")
    created = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.title

