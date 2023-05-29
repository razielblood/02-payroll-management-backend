from django.db import models


class PositionLevel(models.Model):

    name = models.CharField(max_length=64)
    description = models.CharField(max_length=512)

    def __str__(self):
        return self.name
