from django.db import models


class Position(models.Model):
    """"
    Just a Position model that stores the name of the Position
    """
    position_name = models.CharField(max_length=30)


class Employee(models.Model):
    """"
    A model of Employee that contains:
        -Firstname, Lastname, Patronymic and Photo
        -The ManyToMany reference to Department table to register bosses for departments
    """
    firstname = models.CharField(max_length=30)
    lastname = models.CharField(max_length=30)
    patronymic = models.CharField(max_length=30)
    photo = models.ImageField(null=True, blank=True)
    ruling_departments = models.ManyToManyField('Department', blank=True)

    def __str__(self):
        return [self.lastname, self.firstname, self.patronymic].join(' ')


class Department(models.Model):
    """
    A model of Department that contains:
        -Department name
        -The ManyToOne reference to itself (to get the head department)
        -The ManyToOne reference to Organization model (to know to what it belongs)
    """
    department_name = models.CharField(max_length=35)
    head_department = models.ForeignKey('self', null=True,
                                        blank=True, on_delete=models.SET_NULL)
    organization = models.ForeignKey('Organization', null=True,
                                     blank=True, on_delete=models.SET_NULL)

    def __str__(self):
        return self.department_name


class Employee_Department_Position(models.Model):
    """"
        A three hand model that is responsible for registering an employee to the department
    """
    employee = models.ForeignKey(Employee, null=True,
                                 on_delete=models.SET_NULL)
    department = models.ForeignKey(Department, null=True,
                                   on_delete=models.SET_NULL)
    position = models.ForeignKey(Position, null=True,
                                 on_delete=models.SET_NULL)

    class Meta:
        unique_together = ("employee", "department", "position")


class Employee_Headman_Position(models.Model):
    """"
    A three hand model that is responsible for registering a subordinate to the boss
    """
    employee = models.ForeignKey(Employee, null=True,
                                 on_delete=models.SET_NULL, related_name='worker')
    headman = models.ForeignKey(Employee, null=True,
                                on_delete=models.SET_NULL)
    position = models.ForeignKey(Position,
                                 null=True, on_delete=models.SET_NULL)

    class Meta:
        unique_together = ("employee", "headman", "position")


class Organization(models.Model):
    """"
    A Django model for Organization that stores:
        -The name of organization
        -The departments of organization
    """
    organization_name = models.CharField(max_length=35)

    def __str__(self):
        return self.organization_name
