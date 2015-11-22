from django.conf.urls import url

from . import views

urlpatterns = [
    url(r'^$', views.index, name='index'),
    url(r'^add/$', views.addDisease, name='add'),
    url(r'^setAvail/$', views.setAvailability, name='setAvail'),
    # url(r'^logout/$', views.user_logout, name='logout'),
    # url(r'^register/$', views.register, name='register'),
]
