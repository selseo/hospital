from .models import Department, timeTable, Appointment 
from rest_framework import serializers


class DepartmentSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Department
        fields = ('url', 'name')

# class timeTableSerializer(serializers.HyperlinkedModelSerializer):
#     class Meta:
#         model = timeTable
#         fields = ('url','doctor_id','date','period','patientnum','objects')

# class AppointmentSerializer(serializers.HyperlinkedModelSerializer):
# 	timetable_id = timeTableSerializer();
#     class Meta:
#         model = Appointment
#         fields = ('url', 'patient_id','timetable_id','symptom','cause')