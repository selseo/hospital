from django.conf.urls import url, include
from Visit import views
from Visit.roles.nurse import views as nurse

urlpatterns = [
	url(r'^$', views.index),
	url(r'^seed/$', views.seed),

    url(r'^nurse/$', nurse.index, name='nurse-index'),
    url(r'^nurse/view$', nurse.view, name='nurse-view'),


]