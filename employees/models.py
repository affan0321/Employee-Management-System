# from django.db import models
# from .models import Employee

# class Employee(models.Model):
#     id = models.AutoField(primary_key=True)
#     name = models.CharField(max_length=100)
#     position = models.CharField(max_length=50)
#     department = models.CharField(max_length=50)
#     contact = models.CharField(max_length=20)

#     def __str__(self):
#         return self.name

# class Attendance(models.Model):
#     employee = models.ForeignKey(Employee, on_delete=models.CASCADE)
#     date = models.DateField(auto_now_add=True)

#     def __str__(self):
#         return f"{self.employee.name} - {self.date}"
    
# class Performance(models.Model):
#     employee = models.ForeignKey(Employee, on_delete=models.CASCADE)
#     tasks_completed = models.IntegerField(default=0)
#     productivity_score = models.FloatField(default=0.0)

#     def __str__(self):
#         return f"{self.employee.name} - {self.tasks_completed} tasks"    


from django.db import models
# from employees.models import Employee
from django.contrib.auth.models import User 

# class Employee(models.Model):
#     User = models.OneToOneField(User, on_delete=models.CASCADE)  # ✅ Link Employee to Django User
#     name = models.CharField(max_length=100)
#     id = models.AutoField(primary_key=True)
#     name = models.CharField(max_length=100)
#     position = models.CharField(max_length=50)
#     department = models.CharField(max_length=50)
#     contact = models.CharField(max_length=20)

#     def __str__(self):
#         return self.name

# class Employee(models.Model):
#     user = models.OneToOneField(User, on_delete=models.CASCADE, null=True, blank=True)  # ✅ Temporary fix
#     id = models.AutoField(primary_key=True)
#     name = models.CharField(max_length=100)
#     position = models.CharField(max_length=50)
#     department = models.CharField(max_length=50)
#     contact = models.CharField(max_length=20)

#     def __str__(self):
#         return self.name

class Employee(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, null=True, blank=True)  # ✅ Allow nullable user
    name = models.CharField(max_length=100)
    position = models.CharField(max_length=50)
    department = models.CharField(max_length=50)
    contact = models.CharField(max_length=20)
    hire_date = models.DateField(null=True, blank=True) 

    def __str__(self):
        return self.name


class Attendance(models.Model):
    employee = models.ForeignKey(Employee, on_delete=models.CASCADE)
    date = models.DateField(auto_now_add=True)

    def __str__(self):
        return f"{self.employee.name} - {self.date}"

class Performance(models.Model):
    employee = models.ForeignKey(Employee, on_delete=models.CASCADE)
    tasks_completed = models.IntegerField(default=0)
    productivity_score = models.FloatField(default=0.0)

    def __str__(self):
        return f"{self.employee.name} - {self.tasks_completed} tasks"
    
from employees.models import Employee

class Payroll(models.Model):
    employee = models.ForeignKey(Employee, on_delete=models.CASCADE)
    base_salary = models.DecimalField(max_digits=10, decimal_places=2)
    overtime_hours = models.DecimalField(max_digits=5, decimal_places=2, default=0)
    overtime_rate = models.DecimalField(max_digits=5, decimal_places=2, default=500)  # ₹500 per hour
    deductions = models.DecimalField(max_digits=10, decimal_places=2, default=0)
    pay_date = models.DateField(auto_now_add=True)

    @property
    def total_salary(self):
        return self.base_salary + (self.overtime_hours * self.overtime_rate) - self.deductions

    def __str__(self):
        return f"Payroll for {self.employee.name} - ₹{self.total_salary}"
    

from employees.models import Employee
class Leave(models.Model):
    LEAVE_TYPES = [
        ("Sick", "Sick Leave"),
        ("Vacation", "Vacation Leave"),
        ("Casual", "Casual Leave"),
    ]
    
    employee = models.ForeignKey(Employee, on_delete=models.CASCADE)
    leave_type = models.CharField(max_length=20, choices=LEAVE_TYPES)
    start_date = models.DateField()
    end_date = models.DateField()
    reason = models.TextField(null=True, blank=True)
    status = models.CharField(max_length=20, default="Pending")  # ✅ Default status is "Pending"
    remaining_leaves = models.IntegerField(default=12)  # ✅ Track leave balance

    def __str__(self):
        return f"{self.employee.name} - {self.leave_type} ({self.status})"