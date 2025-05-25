"""
URL configuration for backend project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
# from django.contrib import admin
# # from django.urls import path
# from django.urls import path, include
# from rest_framework.routers import DefaultRouter
# from employees.views import EmployeeViewSet, AttendanceViewSet



# router = DefaultRouter()
# router.register(r'employees', EmployeeViewSet)
# router.register(r'attendance', AttendanceViewSet)

# urlpatterns = [
#     path('admin/', admin.site.urls),
#     path('api/', include(router.urls)),
# ]


from django.contrib import admin
from django.urls import path, include
from rest_framework.routers import DefaultRouter
# from employees.views import EmployeeViewSet, AttendanceViewSet, LeaveViewSet, PayrollViewSet,PerformanceViewSet,generate_pay_slip,PayrollViewSetLeaveViewSet, approve_leave, reject_leave
from employees.views import EmployeeViewSet, AttendanceViewSet, LeaveViewSet, PayrollViewSet, PerformanceViewSet, generate_pay_slip, approve_leave, reject_leave,hiring_trends, attendance_reports


# Create a router for API endpoints
router = DefaultRouter()
router.register(r'employees', EmployeeViewSet)
router.register(r'attendance', AttendanceViewSet)
router.register(r'performance', PerformanceViewSet) 
router.register(r'payroll', PayrollViewSet)
router.register(r'leave', LeaveViewSet)

# Define a basic homepage view
from django.http import HttpResponse
def homepage(request):
    return HttpResponse("<h1>Welcome to Employee Management System</h1>")

urlpatterns = [
    path('admin/', admin.site.urls),  # Django Admin Panel
    path('api/', include(router.urls)),  # API Endpoints for Employee & Attendance
    path('', homepage),  # Default homepage route
    path("api/payroll/<int:payroll_id>/pay-slip/", generate_pay_slip, name="generate_pay_slip"),
    path("api/leave/<int:leave_id>/approve/", approve_leave, name="approve_leave"),
    path("api/leave/<int:leave_id>/reject/", reject_leave, name="reject_leave"),
    path("api/hiring-trends/", hiring_trends, name="hiring-trends"),
    path("api/attendance-reports/", attendance_reports, name="attendance-reports"),
]
