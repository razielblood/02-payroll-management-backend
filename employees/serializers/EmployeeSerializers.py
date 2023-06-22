from rest_framework.serializers import ModelSerializer, SerializerMethodField, ValidationError

from employees.models import Employee, PositionAssignment
from employees.serializers import ListPositionAssignmentSerializer

from datetime import datetime


class ListEmployeeSerializer(ModelSerializer):
    current_position = SerializerMethodField()

    def get_current_position(self, obj):
        current_position = PositionAssignment.objects.filter(employee=obj, end_date__isnull=True).first()
        if current_position:
            return ListPositionAssignmentSerializer(current_position).data
        return None
    
    def validate_date_of_birth(self, date_of_birth):
        """Check that te date of birth is in the past.
        """
        if date_of_birth > datetime.now().date():
            raise ValidationError("Date of birth is in the future")

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
