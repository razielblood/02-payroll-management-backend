from rest_framework.generics import ListCreateAPIView, RetrieveUpdateAPIView
from employees.serializers import ListEmployeeSerializer, ListPositionAssignmentSerializer
from employees.models import Employee, PositionAssignment


class ListCreateEmployee(ListCreateAPIView):
    serializer_class = ListEmployeeSerializer
    queryset = Employee.objects.all()


class RetrieveUpdateEmployee(RetrieveUpdateAPIView):
    serializer_class = ListEmployeeSerializer
    queryset = Employee.objects.all()


class ListCreateEmployeePosition(ListCreateAPIView):
    serializer_class = ListPositionAssignmentSerializer

    def get_queryset(self):
        employee_id = self.kwargs["employee_id"]
        employee = Employee.objects.get(pk=employee_id)
        return PositionAssignment.objects.filter(employee=employee)

    def perform_create(self, serializer):
        employee_id = self.kwargs["employee_id"]
        employee = Employee.objects.get(pk=employee_id)
        serializer.save(employee=employee)
