from rest_framework import serializers
from .models import Employees, Departments

class EmployeeSerializer(serializers.ModelSerializer):
    class Meta:
        model = Employees
        fields = ('EmployeeId', 
                  'EmployeeName',
                  'Department',
                  'DateOfJoining',
                  'PhotoFileName'
                  )


class DepartmentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Departments
        fields = ('DepartmentId', 'DepartmentName') 
