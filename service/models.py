from django.db import models
from customer.models import Customer, Payment, Vehicle as CustomerVeh
from vendor.models import Company, Contact

# Service-type labels
class Type(models.Model):
    name = models.CharField(max_length=256, null=True, blank=True)
    description = models.CharField(max_length=512, null=True, blank=True)
    difficulty_level = models.CharField(max_length=25, null=True, blank=True)
    completion_time_in_mins = models.IntegerField()

# These issues can be anything from a flat tire to a dead battery
# Issues are children of service.Type; when a user selects their
# service type the system will display known issues associated
# with that service type
class Issue(models.Model):
    service_type = models.ForeignKey(Type, on_delete=models.CASCADE)
    name = models.CharField(max_length=100)
    description = models.CharField(max_length=500)

# Service tickets
class Ticket(models.Model):
    customer = models.ForeignKey(Customer, on_delete=models.CASCADE)
    company = models.ForeignKey(Company, on_delete=models.CASCADE)
    payment = models.ForeignKey(Payment, on_delete=models.CASCADE)
    service_type = models.ForeignKey(Type, on_delete=models.CASCADE)
    customer_vehicle_id = models.ForeignKey(CustomerVeh, on_delete=models.CASCADE)
    technician = models.ForeignKey(Contact, on_delete=models.CASCADE)
    ticket_no = models.BigAutoField(primary_key=True, unique=True)
    transaction_id = models.CharField(max_length=256)
    transaction_date_time = models.DateTimeField(auto_now=True)
    price = models.DecimalField(max_digits=10, decimal_places=2, null=True, blank=True)
    service_date = models.DateField()
    service_time = models.TimeField()
    is_asap_request = models.BooleanField(default=False)
    # Use All Data for job times for labor hour automation
    labor_hours = models.IntegerField()
    total_labor_cost = models.DecimalField(max_digits=7, decimal_places=2)
    parts_cost = models.DecimalField(max_digits=7, decimal_places=2)
    gratuity = models.DecimalField(max_digits=7, decimal_places=2)
    tech_notes = models.CharField(max_length=1000)
    customer_notes = models.CharField(max_length=1000)

class Part(models.Model):
    ticket_id = models.ForeignKey(Ticket, on_delete=models.CASCADE)
    number = models.CharField(max_length=100)
    name = models.CharField(max_length=100)
    part_description = models.CharField(max_length=150)
    brand = models.CharField(max_length=50)
    pried_at = models.DecimalField(max_digits=6, decimal_places=2)
    cost = models.DecimalField(max_digits=6, decimal_places=2)

# Service reviews from customers
class Review(models.Model):
    ticket_no = models.ForeignKey(Ticket, on_delete=models.CASCADE)
    stars = models.DecimalField(max_digits=4, decimal_places=2)
    comment = models.CharField(max_length=2560, null=True, blank=True)
