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
from employees.views import EmployeeViewSet, AttendanceViewSet,PerformanceViewSet

# Create a router for API endpoints
router = DefaultRouter()
router.register(r'employees', EmployeeViewSet)
router.register(r'attendance', AttendanceViewSet)
router.register(r'performance', PerformanceViewSet) 

# Define a basic homepage view
from django.http import HttpResponse
def homepage(request):
    return HttpResponse("<h1>Welcome to Employee Management System</h1>")

urlpatterns = [
    path('admin/', admin.site.urls),  # Django Admin Panel
    path('api/', include(router.urls)),  # API Endpoints for Employee & Attendance
    path('', homepage),  # Default homepage route
]
