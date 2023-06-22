from rest_framework.generics import ListCreateAPIView, RetrieveUpdateAPIView
from positions.models import PositionLevel
from positions.serializers import ListPositionLevelSerializer


class ListCreatePositionLevelView(ListCreateAPIView):
    serializer_class = ListPositionLevelSerializer
    queryset = PositionLevel.objects.all()
