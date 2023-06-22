from django.test import TestCase
from employees.models import Employee, PositionAssignment
from positions.models import Position, PositionLevel
from employees.serializers import ListEmployeeSerializer
from rest_framework.serializers import ValidationError


class EmployeeSerializerTestCase(TestCase):
    TEST_EMPLOYEES = [
        {
            "id_number": 1,
            "first_name": "Arturo",
            "last_name": "Gomez",
            "email": "a.gomez@example.com",
            "contact_number": "3115689745",
            "date_of_birth": "1991-10-31",
        },
        {
            "id_number": 2,
            "first_name": "Luis",
            "middle_name": "Antonio",
            "last_name": "Perez",
            "email": "l.a.perez@example.com",
            "contact_number": "3174698562",
            "date_of_birth": "1990-01-01",
        },
        {
            "id_number": 3,
            "first_name": "Andrea",
            "last_name": "Lopez",
            "email": "a.lopez@example.com",
            "contact_number": "3225432556",
            "date_of_birth": "1990-01-01",
        },
        {
            "id_number": 4,
            "first_name": "Johanna",
            "last_name": "Gil",
            "email": "j.gil@example.com",
            "contact_number": "3152687598",
            "date_of_birth": "1990-01-01",
        },
        {
            "id_number": 5,
            "first_name": "Carlos",
            "last_name": "Reina",
            "email": "c.reina@example.com",
            "contact_number": "3006249835",
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

        employee_data = {
            "id_number": 20,
            "first_name": "Arturo",
            "last_name": "Gomez",
            "email": "a.gomez@example.com",
            "contact_number": "3124464315",
            "date_of_birth": "2001-01-01",
        }
        employee = Employee.objects.create(**employee_data)
        junior_level, _ = PositionLevel.objects.get_or_create(name="Junior", description="Starting level")
        intermediate_level, _ = PositionLevel.objects.get_or_create(
            name="Intermediate", description="Intermediate level"
        )
        senior_level, _ = PositionLevel.objects.get_or_create(name="Senior", description="Senior level")

        developer_junior, _ = Position.objects.get_or_create(
            name="Developer",
            level=junior_level,
        )
        developer_intermediate, _ = Position.objects.get_or_create(
            name="Developer",
            level=intermediate_level,
        )
        developer_senior, _ = Position.objects.get_or_create(
            name="Developer",
            level=senior_level,
        )
        PositionAssignment.objects.create(
            employee=employee, position=developer_junior, start_date="20150101", end_date="20151231"
        )
        PositionAssignment.objects.create(
            employee=employee, position=developer_intermediate, start_date="20160101", end_date="20181231"
        )
        PositionAssignment.objects.create(
            employee=employee, position=developer_senior, start_date="20180101", end_date=None
        )

    def test_ListSerialization(self):
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
            self.assertEqual(data["current_position"]["position_description"]["name"], "Developer")
            self.assertEqual(data["current_position"]["position_description"]["level_name"], "Junior")
            self.assertEqual(data["current_position"]["start_date"], "2023-01-01")
            self.assertIsNone(data["current_position"]["end_date"])

    def test_SerializeFutureDOB(self):
        invalid_employee_data = {
            "id_number": 10,
            "first_name": "Arturo",
            "last_name": "Gomez",
            "email": "a.gomez@example.com",
            "contact_number": "3223097714",
            "date_of_birth": "2125-01-01",
        }

        serialized_invalid_employee = ListEmployeeSerializer(data=invalid_employee_data)

        self.assertRaises(ValidationError, lambda: serialized_invalid_employee.is_valid(raise_exception=True))

    def test_LastPosition(self):
        saved_employee = Employee.objects.get(pk=20)
        deserialized_saved_employee = ListEmployeeSerializer(instance=saved_employee)
        saved_employee_data = deserialized_saved_employee.data
        self.assertEqual(saved_employee_data["current_position"]["position_description"]["name"], "Developer")
        self.assertEqual(saved_employee_data["current_position"]["position_description"]["level_name"], "Senior")

    def test_InvalidContactNumber(self):
        invalid_employee_data = {
            "id_number": 10,
            "first_name": "Arturo",
            "last_name": "Gomez",
            "email": "a.gomez@example.com",
            "contact_number": "1",
            "date_of_birth": "2005-01-01",
        }

        serialized_invalid_employee = ListEmployeeSerializer(data=invalid_employee_data)

        self.assertRaises(ValidationError, lambda: serialized_invalid_employee.is_valid(raise_exception=True))
