from django.db import models

# Create your models here.

from ckeditor.fields import RichTextField

class News(models.Model):
    title = models.CharField(max_length=50)
    content = RichTextField()
    created = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.title

