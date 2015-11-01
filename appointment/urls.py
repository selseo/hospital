from django.conf import settings
#from django.conf.urls import url
from django.conf.urls.static import static

#for restframework
from django.conf.urls import url, include
from rest_framework import routers

from . import views


router = routers.DefaultRouter()
router.register(r'departments',views.DepartmentViewset)
router.register(r'dee',views.DeeViewset)

urlpatterns = [
	url(r'^', include(router.urls)),
    url(r'^api-auth/', include('rest_framework.urls', namespace='rest_framework')),
    url(r'^$',views.index,name='index'),
    url(r'^show/$',views.show,name='show'),
    url(r'^doctor/$',views.doctor,name='index'),
]

if settings.DEBUG:
	urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
