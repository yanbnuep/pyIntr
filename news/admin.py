from django.contrib import admin

# Register your models here.
from .models import News
from .models import coverImg
fields = ['image_thumb']
readonly_fields = ['image_thumb']
admin.site.register(News,coverImg)
