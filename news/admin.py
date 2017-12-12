from django.contrib import admin

# Register your models here.
from .models import News
from .models import MyAdmin

admin.site.register(News, MyAdmin)
