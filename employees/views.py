from django.http import HttpResponse
from reportlab.pdfgen import canvas
from rest_framework import viewsets
from employees.models import Employee,Attendance,Performance,Payroll,Leave
from .serializers import EmployeeSerializer, AttendanceSerializer,PerformanceSerializer,PayrollSerializer,LeaveSerializer
from rest_framework.response import Response
from django.contrib.auth.decorators import login_required, user_passes_test
from rest_framework.permissions import IsAuthenticated
from rest_framework.decorators import api_view
from rest_framework.response import Response
from django.contrib.auth.models import User
from employees import serializers  # ✅ Correct path
from rest_framework.exceptions import ValidationError 
from django.http import JsonResponse
from datetime import datetime
from django.db import models  # ✅ Correct import for Count function




class EmployeeViewSet(viewsets.ModelViewSet):
    queryset = Employee.objects.all()
    serializer_class = EmployeeSerializer
    # permission_classes = [IsAuthenticated,IsAdmin] 

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

class PayrollViewSet(viewsets.ModelViewSet):
    queryset = Payroll.objects.all()
    serializer_class = PayrollSerializer
    permission_classes = [IsAuthenticated]

def generate_pay_slip(request, payroll_id):
    payroll = Payroll.objects.get(id=payroll_id)

    response = HttpResponse(content_type='application/pdf')
    response['Content-Disposition'] = f'attachment; filename="{payroll.employee.name}_pay_slip.pdf"'

    p = canvas.Canvas(response)
    p.drawString(100, 800, f"Pay Slip for {payroll.employee.name}")
    p.drawString(100, 780, f"Base Salary: {payroll.base_salary}")
    p.drawString(100, 760, f"Overtime Hours: {payroll.overtime_hours} x {payroll.overtime_rate}")
    p.drawString(100, 740, f"Deductions: {payroll.deductions}")
    p.drawString(100, 720, f"Total Salary: {payroll.total_salary}")
    p.showPage()
    p.save()

    return response


class LeaveViewSet(viewsets.ModelViewSet):
    queryset = Leave.objects.all()
    serializer_class = LeaveSerializer
    permission_classes = [IsAuthenticated]  # ✅ Allow authenticated employees to request leave

    def perform_create(self, serializer):
        try:
            user = self.request.user
            employee = Employee.objects.get(user=user)  # ✅ Fetch employee using logged-in user
            serializer.save(employee=employee)
        except Employee.DoesNotExist:
            raise ValidationError({"error": "Employee profile does not exist for this user."})  # ✅ Correct import


@api_view(['POST'])
def approve_leave(request, leave_id):
    try:
        leave = Leave.objects.get(id=leave_id)
        leave.status = "Approved"
        leave.remaining_leaves -= (leave.end_date - leave.start_date).days  # ✅ Deduct leave days
        leave.save()
        return Response({"message": "Leave Approved"})
    except Leave.DoesNotExist:
        return Response({"error": "Leave Request Not Found"}, status=404)

@api_view(['POST'])
def reject_leave(request, leave_id):
    try:
        leave = Leave.objects.get(id=leave_id)
        leave.status = "Rejected"
        leave.save()
        return Response({"message": "Leave Rejected"})
    except Leave.DoesNotExist:
        return Response({"error": "Leave Request Not Found"}, status=404)
    
def hiring_trends(request):
    hiring_data = Employee.objects.extra(select={'month': "strftime('%m', hire_date)"}).values('month').annotate(count=models.Count('id'))
    return JsonResponse(list(hiring_data), safe=False)

# ✅ Attendance Reports API
def attendance_reports(request):
    attendance_data = Attendance.objects.values('date').annotate(attendance=models.Count('id'))
    return JsonResponse(list(attendance_data), safe=False)    

# @api_view(['POST'])
# def approve_leave(request, leave_id):
#     try:
#         leave = Leave.objects.get(id=leave_id)
#         leave.status = "Approved"
#         leave.remaining_leaves -= (leave.end_date - leave.start_date).days  # ✅ Deduct approved leave days
#         leave.save()
#         return Response({"message": "Leave Approved"})
#     except Leave.DoesNotExist:
#         return Response({"error": "Leave Request Not Found"}, status=404)

# @api_view(['POST'])
# def reject_leave(request, leave_id):
#     try:
#         leave = Leave.objects.get(id=leave_id)
#         leave.status = "Rejected"
#         leave.save()
#         return Response({"message": "Leave Rejected"})
#     except Leave.DoesNotExist:
#         return Response({"error": "Leave Request Not Found"}, status=404)        

# def is_admin(user):
#     return user.groups.filter(name='Admin').exists()

# def is_manager(user):
#     return user.groups.filter(name='Manager').exists()

# @login_required
# @user_passes_test(is_admin)
# def admin_dashboard(request):
#     return HttpResponse("Welcome Admin!")

# @login_required
# @user_passes_test(is_manager)
# def manager_dashboard(request):
#     return HttpResponse("Welcome Manager!")