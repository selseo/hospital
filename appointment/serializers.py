from .models import Department, Dee
from rest_framework import serializers


class DepartmentSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Department
        fields = ('url', 'name')


class DeeSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Dee
        fields = ('url', 'name')