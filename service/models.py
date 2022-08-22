from django.db import models
from customer.models import Account, Payment
from vendor.models import Company

# Service-type labels
class Type(models.Model):
    name = models.CharField(max_length=256, null=True, blank=True)
    description = models.CharField(max_length=512, null=True, blank=True)
    difficulty_level = models.CharField(max_length=25, null=True, blank=True)
    completion_time_in_mins = models.IntegerField()

# Service tickets
class Ticket(models.Model):
    ticket_no = models.BigAutoField(primary_key=True, unique=True)
    service_type = models.ForeignKey(Type, on_delete=models.CASCADE)
    customer = models.ForeignKey(Account, on_delete=models.CASCADE)
    company = models.ForeignKey(Company, on_delete=models.CASCADE)
    payment = models.ForeignKey(Payment, on_delete=models.CASCADE)
    transaction_id = models.CharField(max_length=256)
    transaction_date_time = models.DateTimeField(auto_now=True)
    price = models.DecimalField(max_digits=10, decimal_places=2, null=True, blank=True)

# Service reviews from customers
class Review(models.Model):
    ticket_no = models.ForeignKey(Ticket, on_delete=models.CASCADE)
    stars = models.DecimalField(max_digits=4, decimal_places=2)
    comment = models.CharField(max_length=2560, null=True, blank=True)

# Cities that Roadside App operates
class City(models.Model):
    name = models.CharField(max_length=75)
    country = models.CharField(max_length=75)
    nickname = models.CharField(max_length=75)

# Zip codes that fall within a city
class CityZip(models.Model):
    city = models.ForeignKey(City, on_delete=models.CASCADE)
    neighborhood = models.CharField(max_length=75)
    zip_code = models.CharField(max_length=20)
