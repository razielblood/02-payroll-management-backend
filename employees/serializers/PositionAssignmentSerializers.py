from rest_framework.serializers import ModelSerializer, SerializerMethodField
from employees.models import PositionAssignment
from positions.models import Position
from positions.serializers import ListPositionSerializer


class ListPositionAssignmentSerializer(ModelSerializer):
    position = SerializerMethodField()

    def get_position(self, obj):
        position = Position.objects.get(pk=obj.position.id)
        if position:
            return ListPositionSerializer(position).data
        return None

    class Meta:
        model = PositionAssignment
        fields = ["position", "start_date", "end_date"]
