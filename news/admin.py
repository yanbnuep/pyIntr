from django.contrib import admin

# Register your models here.
from .models import News
fields = ['image_tag']
readonly_fields = ['image_tag']

admin.site.register(News)
