from .models import Department, timeTable, Appointment 
from rest_framework import serializers


class DepartmentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Department
        fields = '__all__'

# class timeTableSerializer(serializers.ModelSerializer):
#     class Meta:
#         model = timeTable
#         fields = '__all__'

# class AppointmentSerializer(serializers.HyperlinkedModelSerializer):
# 	timetable_id = timeTableSerializer();
#     class Meta:
#         model = Appointment
#         fields = '__all__'