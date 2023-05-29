from django.db import models

from positions.models import Position

# Create your models here.


class Employee(models.Model):
    """_summary_
    """
    id_number = models.IntegerField(primary_key=True)
    first_name = models.CharField(max_length=64)
    middle_name = models.CharField(max_length=64, blank=True)
    last_name = models.CharField(max_length=64)
    email = models.EmailField()
    contact_number = models.IntegerField()
    date_of_birth = models.DateField()
    positions = models.ManyToManyField(Position, through='PositionAssignment')

    def __str__(self):
        return f'{self.last_name}, {self.first_name}'
