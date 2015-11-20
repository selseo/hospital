from django.conf.urls import url, include
from Visit import views
from Visit.views import views as nurse

urlpatterns = [
    url(r'^nurse/$', nurse.index, name='index'),
]