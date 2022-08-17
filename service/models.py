from django.db import models
from customer.models import Account

class ServiceType(models.Model):
    name = models.CharField(max_length=256)
    description = models.CharField(max_length=512)
    difficulty_level = models.CharField(max_length=25)
    completion_time_in_mins = models.IntegerField()


class Service(models.Model):
    ticket_no = models.BigAutoField(primary_key=True, unique=True)
    service_type = models.ForeignKey(ServiceType, on_delete=models.CASCADE)
    customer = models.ForeignKey(Account, on_delete=models.CASCADE)
    # company = models.ForeignKey(Company, on_delete=models.CASCADE)
    price = models.DecimalField(max_digits=10, decimal_places=2)
    # payment?


class ServiceReview(models.Model):
    ticket_no = models.ForeignKey(Service, on_delete=models.CASCADE)
    stars = models.DecimalField(max_digits=4, decimal_places=2)


