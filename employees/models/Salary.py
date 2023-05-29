from django.db import models
from employees.models import Employee


class Salary(models.Model):
    """_summary_
    """

    effective_date = models.DateField()
    salary_value = models.IntegerField()
    update_date = models.DateField(auto_now=True)
    employee = models.ForeignKey(
        Employee, on_delete=models.PROTECT, related_name='salaries')

    def __str__(self):
        return f'{self.employee.last_name}, {self.employee.first_name} - {self.salary_value} [{self.effective_date}]'
