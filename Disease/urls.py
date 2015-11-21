from django.conf.urls import url

from . import views

urlpatterns = [
    #url(r'^register/$', views.nptregform, name='register'),
    #url(r'^register/submit/$', views.submit, name='submit'),
    url(r'^$', views.index, name='index'),
    url(r'^add/$', views.addDisease, name='add'),
    url(r'^setAvail/$', views.setAvailability, name='setAvail'),
    # url(r'^logout/$', views.user_logout, name='logout'),
    # url(r'^register/$', views.register, name='register'),
    
]
