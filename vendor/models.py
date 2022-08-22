from django.db import models
from service.models import City, Type

class Company(models.Model):
    name = models.CharField(max_length=100, null=True, blank=True)

class Vehicle(models.Model):
    make = models.CharField(max_length=50)
    model = models.CharField(max_length=50)
    year = models.CharField(max_length=4)
    color = models.CharField(max_length=50)
    tag_state = models.CharField(max_length=2)
    tag_no = models.CharField(max_length=12)

class Contact(models.Model):
    vehicle = models.ForeignKey(Vehicle, on_delete=models.CASCADE)
    company = models.ForeignKey(Company, on_delete=models.CASCADE)
    first_name = models.CharField(max_length=75)
    last_name = models.CharField(max_length=75)
    email = models.CharField(max_length=100)
    main_phone = models.CharField(max_length=20)
    main_phone_ext = models.CharField(max_length=10)
    secondary_phone = models.CharField(max_length=20)
    secondary_phone_ext = models.CharField(max_length=10)

class CompanyService(models.Model):
    type = models.ForeignKey(Type, on_delete=models.CASCADE)
    city = models.ForeignKey(City, on_delete=models.CASCADE)
    company = models.ForeignKey(Company, on_delete=models.CASCADE)
