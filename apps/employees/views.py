from drf_spectacular.utils import extend_schema
from rest_framework.viewsets import ModelViewSet

from apps.employees.models import Employee, Attendance, Salary
from apps.employees.serializers import EmployeeSerializer, AttendanceSerializer, SalarySerializer


@extend_schema(tags=["employee-api"])
class EmployeeViewSet(ModelViewSet):
    queryset = Employee.objects.all()
    serializer_class = EmployeeSerializer


@extend_schema(tags=["attendance-api"])
class AttendanceViewSet(ModelViewSet):
    queryset = Attendance.objects.all()
    serializer_class = AttendanceSerializer


@extend_schema(tags=["salary-api"])
class SalaryViewSet(ModelViewSet):
    queryset = Salary.objects.all()
    serializer_class = SalarySerializer
