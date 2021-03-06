from django.conf import settings
#from django.conf.urls import url
from django.conf.urls.static import static

#for restframework
from django.conf.urls import url, include
from rest_framework import routers

from . import views


router = routers.DefaultRouter()
router.register(r'departments',views.DepartmentViewset)

urlpatterns = [
    url(r'^', include(router.urls)),
    url(r'^api-auth/', include('rest_framework.urls', namespace='rest_framework')),
    url(r'^$',views.index,name='index'),
    url(r'^show/$',views.show,name='show'),
    url(r'^show/bystaff$',views.appointmentbystaff,name='appointmentbystaff'),
    url(r'^doctor/$',views.doctor,name='index'),
    url(r'^editappointment/$',views.editappointment,name='editappointment'),
    url(r'^editappointment/bystaff/$',views.patientsearchforapp,name='patientsearchforapp'),
    url(r'^editappointment/bystaff/(?P<pid>[0-9]+)/$',views.editappointmentbystaff,name='editappointmentbystaff'),
    url(r'^editappointment/reschedule/(?P<aid>[0-9]+)/$',views.reschedule,name='reschedule'),
    url(r'^editappointment/cancel/(?P<aid>[0-9]+)/$',views.cancel,name='cancel'),
    url(r'^patientlist/$',views.patientlist,name='patientlist'),
    url(r'^getpatientlist/$',views.getpatientlist),
    url(r'^getdoctorlist/$',views.getdoctorlist),
    url(r'^getappointmentlist/$',views.getappointmentlist),
    url(r'^getpatientappointment/$',views.getpatientappointment),
    url(r'^timetable/$',views.timetable,name='timetable'),
    url(r'^gettimetable/$',views.gettimetable),
    url(r'^savetimetable/$',views.savetimetable),
    url(r'^searchpatient/$',views.searchpatient),
    url(r'^seed/$',views.seed),
]

if settings.DEBUG:
	urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
