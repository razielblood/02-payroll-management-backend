from rest_framework.serializers import ModelSerializer, PrimaryKeyRelatedField, SerializerMethodField

from employees.models import Employee, PositionAssignment
from employees.serializers import ListPositionAssignmentSerializer


class ListEmployeeSerializer(ModelSerializer):
    current_position = SerializerMethodField()

    def get_current_position(self, obj):
        current_position = PositionAssignment.objects.filter(employee=obj, end_date__isnull=True).first()
        if current_position:
            return ListPositionAssignmentSerializer(current_position).data
        return None

    class Meta:
        model = Employee
        fields = [
            "id_number",
            "first_name",
            "middle_name",
            "last_name",
            "current_position",
            "email",
            "contact_number",
            "date_of_birth",
        ]
