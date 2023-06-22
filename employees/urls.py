from django.urls import path
from employees.views import ListCreateEmployee, RetrieveUpdateEmployee, ListCreateEmployeePosition

urlpatterns = [
    path("employees/", ListCreateEmployee.as_view(), name="employees"),
    path("employees/<int:pk>", RetrieveUpdateEmployee.as_view(), name="employee"),
    path("employees/<int:employee_id>/positions", ListCreateEmployeePosition.as_view(), name="employee"),
]
