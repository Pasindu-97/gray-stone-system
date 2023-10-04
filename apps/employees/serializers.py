from rest_framework import serializers

from apps.employees.models import Employee, Attendance, Salary


class EmployeeSerializer(serializers.ModelSerializer):
    class Meta:
        model = Employee
        fields = "__all__"
        read_only_fields = ("id", "created", "modified", "created_by")


class AttendanceSerializer(serializers.ModelSerializer):
    class Meta:
        model = Attendance
        fields = "__all__"
        read_only_fields = ("id", "created", "modified", "created_by")


class SalarySerializer(serializers.ModelSerializer):
    class Meta:
        model = Salary
        fields = "__all__"
        read_only_fields = ("id", "created", "modified", "created_by")
