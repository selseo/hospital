from django.contrib import admin
from .models import Department
from .models import Dee
from .models import Doctor
from .models import timeTable

# Register your models here.
admin.site.register(Department)

admin.site.register(Dee)
admin.site.register(Doctor)
admin.site.register(timeTable)