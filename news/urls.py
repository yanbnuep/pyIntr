from django.conf.urls import include,url

from . import views
urlpatterns = [
    url(r'^$', views.index, name='index'),
    url(r'^ckeditor/', include('ckeditor_uploader.urls')),
    url(r'^(?P<news_id>[0-9]+)/$',views.newsContent,name='newsContent')
]