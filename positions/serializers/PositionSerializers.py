from rest_framework.serializers import ModelSerializer, StringRelatedField
from positions.models import Position


class ListPositionSerializer(ModelSerializer):
    level = StringRelatedField()

    class Meta:
        model = Position
        fields = ["name", "level"]
