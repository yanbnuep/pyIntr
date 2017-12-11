from django.contrib import admin

# Register your models here.
from .models import News
from .models import Cover

admin.site.register(News, Cover)
