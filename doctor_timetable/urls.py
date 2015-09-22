from django.conf.urls import url

from . import views

urlpatterns = [
    url(r'^$', views.index, name='index'),
    url(r'^save/$',views.save, name='save'),
    url(r'^getdata/$',views.getData, name='getData'),
]