from rest_framework import viewsets
# from .models import Employee, Attendance,Performance
from employees.models import Employee,Attendance,Performance

from .serializers import EmployeeSerializer, AttendanceSerializer,PerformanceSerializer
from rest_framework.response import Response

class EmployeeViewSet(viewsets.ModelViewSet):
    queryset = Employee.objects.all()
    serializer_class = EmployeeSerializer

# class AttendanceViewSet(viewsets.ModelViewSet):
#     queryset = Attendance.objects.all()
#     serializer_class = AttendanceSerializer


class AttendanceViewSet(viewsets.ModelViewSet):
    queryset = Attendance.objects.all()
    serializer_class = AttendanceSerializer

    def create(self, request, *args, **kwargs):
        employee_id = request.data.get("employee")
        if not employee_id:
            return Response({"error": "Employee ID is required"}, status=400)

        try:
            employee = Employee.objects.get(id=employee_id)
        except Employee.DoesNotExist:
            return Response({"error": "Employee not found"}, status=404)

        attendance = Attendance.objects.create(employee=employee)
        return Response(AttendanceSerializer(attendance).data, status=201)
    
class PerformanceViewSet(viewsets.ModelViewSet):
    queryset = Performance.objects.all()
    serializer_class = PerformanceSerializer    