from django.db import models
from django.utils.html import format_html
from django.utils.safestring import mark_safe
from django.contrib import admin
# Create your models here.
from ckeditor_uploader.fields import  RichTextUploadingField


class Cover(admin.ModelAdmin):

    def image_tag(self, obj):
        return format_html('<img src="{}" />'.format(obj.image.url))

    image_tag.short_description = 'Image'

    list_display = ['image_tag',]

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

