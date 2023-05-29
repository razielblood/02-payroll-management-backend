from django.contrib import admin
from employees.models import Employee, PositionAssignment, Salary

# Register your models here.
admin.site.register(Employee)
admin.site.register(PositionAssignment)
admin.site.register(Salary)
