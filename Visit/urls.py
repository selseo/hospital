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
    url(r'^doctor/addMedicine/(\d+)$', doctor.addMedicine, name='doctor-add-medicine'), 
    url(r'^doctor/deleteMedicine/(?P<num>\d+)/(?P<medicine_name>[^/]+)$', doctor.deleteMedicine, name='doctor-delete-medicine'),
    url(r'^doctor/addDisease/(\d+)$', doctor.addDisease, name='doctor-add-disease'),
    url(r'^doctor/deleteDisease/(?P<num>\d+)/(?P<ICD10>[^/]+)$', doctor.deleteDisease, name='doctor-delete-disease'),
    url(r'^doctor/view$', doctor.view, name='doctor-view'),
    url(r'^doctor/edit/(\d+)$', doctor.editStatus1, name='doctor-editStatus1'),
    url(r'^pharmacist/$', pharmacist.index, name='pharmacist-index'),
    url(r'^pharmacist/view$', pharmacist.view, name='pharmacist-view'),
    url(r'^pharmacist/edit/(\d+)$', pharmacist.editStatus2, name='pharmacist-editStatus2'),

]