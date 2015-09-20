from django.conf.urls import url

from . import views

urlpatterns = [
    url(r'^register/$', views.nptregform, name='register'),
    url(r'^register/submit/$', views.submit, name='submit'),
]
