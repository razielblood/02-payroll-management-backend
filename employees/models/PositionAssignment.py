from django.db import models

from positions.models import Position


class PositionAssignment(models.Model):
    """_summary_"""

    employee = models.ForeignKey("Employee", on_delete=models.PROTECT, related_name="position")
    position = models.ForeignKey(Position, on_delete=models.PROTECT)
    start_date = models.DateField()
    end_date = models.DateField(null=True, blank=True)

    def __str__(self):
        return f"{self.employee.last_name}, {self.employee.first_name} - {self.position.name} [{self.start_date} - {self.end_date}]"

    class Meta:
        unique_together = ("employee", "position")
