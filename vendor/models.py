from django.db import models

# Cities that Roadside App operates
class City(models.Model):
    name = models.CharField(max_length=75)
    country = models.CharField(max_length=75)

# Zip codes that fall within a city
class CityZip(models.Model):
    city = models.ForeignKey(City, on_delete=models.CASCADE)
    neighborhood = models.CharField(max_length=75)
    zip_code = models.CharField(max_length=20)

class Company(models.Model):
    name = models.CharField(max_length=100, null=True, blank=True)
    hourly_price = models.DecimalField(max_digits=5, decimal_places=2)

class CompanyLocation(models.Model):
    company = models.ForeignKey(Company, on_delete=models.CASCADE)
    city = models.ForeignKey(City, on_delete=models.CASCADE)
    location_nickname = models.CharField(max_length=100)

class Vehicle(models.Model):
    company_location = models.ForeignKey(CompanyLocation, on_delete=models.CASCADE)
    make = models.CharField(max_length=50)
    model = models.CharField(max_length=50)
    year = models.CharField(max_length=4)
    color = models.CharField(max_length=50)
    tag_state = models.CharField(max_length=2)
    tag_no = models.CharField(max_length=12)

class Contact(models.Model):
    vehicle = models.ForeignKey(Vehicle, on_delete=models.CASCADE)
    first_name = models.CharField(max_length=75)
    last_name = models.CharField(max_length=75)
    email = models.CharField(max_length=100)
    main_phone = models.CharField(max_length=20)
    main_phone_ext = models.CharField(max_length=10)
    secondary_phone = models.CharField(max_length=20)
    secondary_phone_ext = models.CharField(max_length=10)
