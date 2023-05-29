from django.db import models
from positions.models.PositionLevel import PositionLevel


class Position(models.Model):
    """_summary_
    """

    name = models.CharField(max_length=64)
    level = models.ForeignKey(
        PositionLevel, on_delete=models.PROTECT, related_name='positions', blank=True)

    def __str__(self):
        return f'{self.name} - [{self.level.name}]'
