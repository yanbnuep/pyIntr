from django.db import models
from django.contrib import admin

# Create your models here.
from ckeditor_uploader.fields import  RichTextUploadingField
from django_resized import ResizedImageField
from django.utils.safestring import mark_safe
from django.contrib.admin.widgets import AdminFileWidget
from datetime import datetime

class News(models.Model):

    title = models.CharField(max_length=50)
    cover = ResizedImageField(upload_to='coverImg/', size=[500, 300])
    content = RichTextUploadingField(blank=True, null=True, verbose_name="context")
    created = models.DateTimeField(auto_now_add=True)
    news_date = models.DateField(default=datetime.now, blank=False)
    def __str__(self):
        return self.title


class AdminImageWidget(AdminFileWidget):

    def render(self, name, value, attrs=None, renderer=None):
        output = []
        if value and getattr(value, "url", None):
            image_url = value.url
            file_name = str(value)
            output.append(u' <a href="%s" target="_blank"><img src="%s" alt="%s" /></a>  ' % \
                (image_url, image_url, file_name))
            output.append(super(AdminFileWidget, self).render(name, value, attrs))
            return mark_safe(u''.join(output))


class MyAdmin(admin.ModelAdmin):
    def formfield_for_dbfield(self, db_field, **kwargs):
        if db_field.name == 'cover':
            request = kwargs.pop("request", None)
            kwargs['widget'] = AdminImageWidget
            return db_field.formfield(**kwargs)
        return super(MyAdmin,self).formfield_for_dbfield(db_field, **kwargs)