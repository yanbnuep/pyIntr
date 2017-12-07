from django.shortcuts import render

# Create your views here.
from django.http import HttpResponse
from .models import News
from django.template import loader

def index(request):
    newsList = News.objects.order_by('-created')[:5]
    context = {
        'newsList': newsList
    }
    return render(request,'/index.html',context)
