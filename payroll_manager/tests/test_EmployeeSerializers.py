from django.test import TestCase
from employees.models import Employee, PositionAssignment
from positions.models import Position, PositionLevel
from employees.serializers import ListEmployeeSerializer


class EmployeeSerializerTestCase(TestCase):
    TEST_EMPLOYEES = [
        {
            "id_number": 1,
            "first_name": "Arturo",
            "last_name": "Gomez",
            "email": "a.gomez@example.com",
            "contact_number": 123456789,
            "date_of_birth": "1991-10-31",
        },
        {
            "id_number": 2,
            "first_name": "Luis",
            "middle_name": "Antonio",
            "last_name": "Perez",
            "email": "l.a.perez@example.com",
            "contact_number": 987654321,
            "date_of_birth": "1990-01-01",
        },
        {
            "id_number": 3,
            "first_name": "Andrea",
            "last_name": "Lopez",
            "email": "a.lopez@example.com",
            "contact_number": 123456789,
            "date_of_birth": "1990-01-01",
        },
        {
            "id_number": 4,
            "first_name": "Johanna",
            "last_name": "Gil",
            "email": "j.gil@example.com",
            "contact_number": 123456789,
            "date_of_birth": "1990-01-01",
        },
        {
            "id_number": 5,
            "first_name": "Carlos",
            "last_name": "Reina",
            "email": "c.reina@example.com",
            "contact_number": 123456789,
            "date_of_birth": "1990-01-01",
        },
    ]

    def setUp(self):
        # Crear objetos de prueba
        self.assignments = list()
        for employee in self.TEST_EMPLOYEES:
            self.assignments.append(
                PositionAssignment.objects.create(
                    employee=Employee.objects.create(**employee),
                    position=Position.objects.get_or_create(
                        name="Developer",
                        level=PositionLevel.objects.get_or_create(name="Junior", description="Starting level")[0],
                    )[0],
                    start_date="2023-01-01",
                    end_date=None,
                )
            )
        map(lambda emp: emp.save(), self.assignments)

    def test_serialization(self):
        # Serializar los objetos de prueba
        for idx, base_employee in enumerate(self.TEST_EMPLOYEES):
            serializer = ListEmployeeSerializer(instance=self.assignments[idx].employee)

            data = serializer.data

            # Verificar los campos serializados de cada empleado
            self.assertEqual(data["id_number"], base_employee["id_number"])
            self.assertEqual(data["first_name"], base_employee["first_name"])
            self.assertEqual(data["last_name"], base_employee["last_name"])
            self.assertEqual(data["email"], base_employee["email"])
            self.assertEqual(data["contact_number"], base_employee["contact_number"])
            self.assertEqual(data["date_of_birth"], base_employee["date_of_birth"])
            self.assertEqual(data["current_position"]["position"]["name"], "Developer")
            self.assertEqual(data["current_position"]["position"]["level"], "Junior")
            self.assertEqual(data["current_position"]["start_date"], "2023-01-01")
            self.assertIsNone(data["current_position"]["end_date"])
