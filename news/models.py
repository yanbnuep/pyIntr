from django.db import models

# Create your models here.
from ckeditor.fields import RichTextFormField

class news(models.Model):
    title = models.CharField(u'title',default='title',max_length=30)
    content = RichTextFormField(u'content', default='',null = True, blank=True)
    updatedTime = models.DateTimeField(u'updateTime', auto_now=True)
