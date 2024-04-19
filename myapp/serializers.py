from rest_framework import serializers
from . import models

class DeptSerializer(serializers.ModelSerializer):
    class Meta:
        model=models.Dept
        fields="__all__"

class EmpSerializer(serializers.ModelSerializer):
    class Meta:
        model=models.Emp
        fields="__all__"