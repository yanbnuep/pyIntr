from django.shortcuts import render

# Create your views here.
from django.http import HttpResponse
from .models import News

def index(request):
    newsList = News.objects.order_by('-created')[:5]
    context = {
        'newsList': newsList
    }
    return render(request,'index.html',context)

def newsContent(request,news_id):
    try:
        news = News.objects.get(pk = news_id)
    except News.DoesNotExist:
        raise HttpResponse(request,"doesn't exist")
    return render(request,'newsContent.html',{'news':news})