from django.conf.urls import url, include
from Visit import views
from Visit.roles.nurse import views as nurse
from Visit.roles.doctor import views as doctor
from Visit.roles.pharmacist import views as pharmacist

urlpatterns = [
	url(r'^$', views.index),
	url(r'^seed/$', views.seed),
    url(r'^nurse/$', nurse.index, name='nurse-index'),
    url(r'^nurse/view$', nurse.view, name='nurse-view'),
    url(r'^nurse/edit/(\d+)$', nurse.editStatus0, name='nurse-editStatus0'),
    url(r'^doctor/$', doctor.index, name='doctor-index'),
    url(r'^doctor/view$', doctor.view, name='doctor-view'),
    url(r'^doctor/edit/(\d+)$', doctor.editStatus1, name='doctor-editStatus1'),
    url(r'^pharmacist/$', pharmacist.index, name='pharmacist-index'),
    url(r'^pharmacist/edit/(\d+)$', pharmacist.editStatus2, name='pharmacist-editStatus2'),

]