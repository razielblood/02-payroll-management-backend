from rest_framework.generics import ListCreateAPIView, RetrieveUpdateAPIView
from positions.models import Position
from positions.serializers import ListPositionSerializer


class ListCreatePositionView(ListCreateAPIView):
    serializer_class = ListPositionSerializer
    queryset = Position.objects.all()
