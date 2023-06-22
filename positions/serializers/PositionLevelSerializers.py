from rest_framework.serializers import ModelSerializer
from positions.models import PositionLevel


class ListPositionLevelSerializer(ModelSerializer):
    class Meta:
        model = PositionLevel
        fields = ["name", "description"]
