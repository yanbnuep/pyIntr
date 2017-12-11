from django.contrib import admin

# Register your models here.
from .models import News

readonly_fields = ['image_tag']

admin.site.register(News)
