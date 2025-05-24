from rest_framework import serializers
# from .models import Employee, Attendance,Performance
from employees.models import Employee, Attendance, Performance



class EmployeeSerializer(serializers.ModelSerializer):
    class Meta:
        model = Employee
        # fields = ['id', 'name']
        fields = ['id', 'name', 'position', 'department', 'contact'] 

class AttendanceSerializer(serializers.ModelSerializer):
    employee = EmployeeSerializer()
    class Meta:
        model = Attendance
        fields = '__all__'

class PerformanceSerializer(serializers.ModelSerializer):
    employee = EmployeeSerializer()  
    class Meta:
        model = Performance
        fields = '__all__'        
