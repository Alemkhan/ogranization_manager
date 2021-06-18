from .models import *
from rest_framework.response import Response
from rest_framework import generics
from appointment import serializers


# Create your views here.
class DepartmentAPIView(generics.ListCreateAPIView):
    serializer_class = serializers.DepartmentSerializer
    queryset = Department.objects.all()


class DepartmentDetailAPIView(generics.RetrieveUpdateDestroyAPIView):
    serializer_class = serializers.DepartmentSerializer
    queryset = Department.objects.all()


class EmployeeAPIView(generics.ListCreateAPIView):
    serializer_class = serializers.EmployeeSerializer
    queryset = Employee.objects.all()


class EmployeeDetailAPIView(generics.RetrieveUpdateDestroyAPIView):
    serializer_class = serializers.EmployeeSerializer
    queryset = Employee.objects.all()


class OrganizationAPIView(generics.ListCreateAPIView):
    serializer_class = serializers.OrganizationSerializer
    queryset = Organization.objects.all()


class OrganizationDetailAPIView(generics.ListCreateAPIView):
    serializer_class = serializers.OrganizationSerializer
    queryset = Organization.objects.all()
