from rest_framework.serializers import ModelSerializer, StringRelatedField, RelatedField
from positions.models import Position


class ListPositionSerializer(ModelSerializer):
    level_name = StringRelatedField(source="level", read_only=True)

    class Meta:
        model = Position
        fields = ["name", "level_name", "level"]
        extra_kwargs = {"level": {"write_only": True}}
