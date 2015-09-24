from django.contrib import admin
from .models import Doctor
from .models import timeTable
# Register your models here.
admin.site.register(Doctor)
admin.site.register(timeTable)