from django.db import models
from django.utils.safestring import mark_safe
# Create your models here.
from ckeditor_uploader.fields import  RichTextUploadingField


class News(models.Model):
    title = models.CharField(max_length=50)
    cover = models.ImageField(upload_to='coverImg/', blank=True)

    def image_tag(self):
        return mark_safe('<br>this url is %s</br>' % self.cover.url)
    image_tag.short_description = 'Image'
    content = RichTextUploadingField(blank=True, null=True, verbose_name="context")
    created = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.title

