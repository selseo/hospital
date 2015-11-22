from django.conf.urls import url

from . import views

urlpatterns = [
    #url(r'^register/$', views.nptregform, name='register'),
    #url(r'^register/submit/$', views.submit, name='submit'),
    url(r'^$', views.index, name='index'),
    url(r'^login/$', views.user_login, name='login'),
    url(r'^restricted/$', views.restricted, name='restricted'),
    url(r'^logout/$', views.user_logout, name='logout'),
    url(r'^register/$', views.register, name='register'),
    url(r'^createuser/$', views.admin_create_user, name='createuser'),

]
