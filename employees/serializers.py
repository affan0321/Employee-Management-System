from rest_framework import serializers
# from .models import Employee, Attendance,Performance
from employees.models import Employee, Attendance, Performance,Payroll,Leave



# class EmployeeSerializer(serializers.ModelSerializer):
#     class Meta:
#         model = Employee
#         # fields = ['id', 'name']
#         # fields = ['id', 'name', 'position']
#         fields = '__all__'  

class EmployeeSerializer(serializers.ModelSerializer):
    class Meta:
        model = Employee
        fields = '__all__'  # ✅ Ensure all fields are included



class AttendanceSerializer(serializers.ModelSerializer):
    employee = EmployeeSerializer()
    class Meta:
        model = Attendance
        fields = '__all__'

# class PerformanceSerializer(serializers.ModelSerializer):
#     employee = EmployeeSerializer()  
#     class Meta:
#         model = Performance
#         fields = '__all__'        


class PerformanceSerializer(serializers.ModelSerializer):
    # employee = serializers.PrimaryKeyRelatedField(queryset=Employee.objects.all())  # ✅ Use Primary Key instead of nested data
    employee = EmployeeSerializer()
    class Meta:
        model = Performance
        fields = '__all__'

class PayrollSerializer(serializers.ModelSerializer):
    total_salary = serializers.ReadOnlyField()

    class Meta:
        model = Payroll
        fields = '__all__'

class LeaveSerializer(serializers.ModelSerializer):
    class Meta:
        model = Leave
        fields = '__all__'        