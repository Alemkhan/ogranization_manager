from rest_framework import serializers
from appointment import models


class HeadDepartmentSerializer(serializers.ModelSerializer):
    """"
    Serializes the Head Department (used for DepartmentSerializer)
    """

    class Meta:
        model = models.Department
        fields = '__all__'


class DepartmentSerializer(serializers.ModelSerializer):
    """"
    Serializes the Department, with recursive gain of Head Department
    """
    head_department = HeadDepartmentSerializer().read_only

    class Meta:
        model = models.Department
        fields = '__all__'


class OrganizationSerializer(serializers.ModelSerializer):
    """"
    Serializes all the organization information including all departments inside
    """
    departments = serializers.SerializerMethodField()

    class Meta:
        model = models.Organization
        fields = '__all__'

    # Get all the departments of the certain organization
    def get_departments(self, obj):
        queryset = models.Department.objects.filter(organization=obj)
        departments_list = []
        for department in queryset:
            departments_list.append(DepartmentSerializer(department).data)
        return departments_list


class PositionSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.Position
        fields = '__all__'


class EmployeeSerializer(serializers.ModelSerializer):
    subordinates = serializers.SerializerMethodField()

    class Meta:
        model = models.Employee
        fields = '__all__'

    # Get all employees that are under the certain boss
    def get_subordinates(self, obj):
        queryset = models.Employee_Headman_Position.objects.filter(headman=obj)
        subordinates_list = []
        for employee in queryset:
            subordinates_list.append(SubordinateOrHeadmanSerializer(employee).data)
        return subordinates_list


class SubordinateOrHeadmanSerializer(serializers.ModelSerializer):
    """"
    Serializes the three handshake model to get Subordinates and Headman of a certain Department
    """
    employee = EmployeeSerializer()

    class Meta:
        model = models.Employee_Headman_Position
        fields = ['employee']
