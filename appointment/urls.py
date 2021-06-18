from django.urls import path, include
from appointment import views

urlpatterns = [
    path('departments/', views.DepartmentAPIView.as_view(), name="departments"),
    path('departments/<int:pk>', views.DepartmentDetailAPIView.as_view(), name="department"),
    path('employees/', views.EmployeeAPIView.as_view(), name="employees"),
    path('employees/<int:pk>', views.EmployeeDetailAPIView.as_view(), name="employee"),
    path('organizations/', views.OrganizationAPIView.as_view(), name="organizations"),
    path('organizations/<int:pk>', views.OrganizationDetailAPIView.as_view(), name="organization"),
]