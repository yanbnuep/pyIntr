from django.conf.urls import url

from . import views
urlpatterns = [
    url('', views.index, name='index'),
    url('<int:news_id>/',views.newsContent,name='newsContent')
]