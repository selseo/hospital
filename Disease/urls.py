from django.conf.urls import url

from . import views

urlpatterns = [
    url(r'^$', views.index, name='index'),
    url(r'^seed/$', views.seed,name='seed'),
    url(r'^add/$', views.addDisease, name='add'),
    url(r'^setAvail/$', views.setAvailability, name='setAvail'),
]
