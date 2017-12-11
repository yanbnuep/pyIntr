from django.db import models

# Create your models here.
from ckeditor_uploader.fields import  RichTextUploadingField
from django.utils.safestring import mark_safe
class News(models.Model):
    title = models.CharField(max_length=50)
    cover = models.ImageField(upload_to='coverImg', blank=True, null=True)
    def image_thumbnail(self):
        return mark_safe('<br>show preview</br><img src="/media/%s" width="150" height="150" />' % (self.cover))
    image_thumbnail.short_description = 'Cover'
    content = RichTextUploadingField(blank=True,null=True,verbose_name="context")
    created = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.title

