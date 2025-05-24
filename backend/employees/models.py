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

class Employee(models.Model):
    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=100)
    position = models.CharField(max_length=50)
    department = models.CharField(max_length=50)
    contact = models.CharField(max_length=20)

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
