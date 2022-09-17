from django.db import models

class Customer(models.Model):
    first_name = models.CharField(max_length=96)
    last_name = models.CharField(max_length=96)
    email = models.CharField(max_length=96)
    main_phone = models.CharField(max_length=20)
    secondary_phone = models.CharField(max_length=20)
    main_account_holder_id = models.ForeignKey('self', on_delete=models.CASCADE)
    created_on = models.DateTimeField(auto_now=True)

class Payment(models.Model):
    account = models.ForeignKey(Customer, on_delete=models.CASCADE)
    authorize_payment_id = models.IntegerField()

class Vehicle(models.Model):
    owner = models.ForeignKey(Customer, on_delete=models.CASCADE, related_name='owner')
    driver = models.ForeignKey(Customer, on_delete=models.CASCADE, related_name='driver')
    make = models.CharField(max_length=64)
    model = models.CharField(max_length=64)
    color = models.CharField(max_length=32)
    year = models.CharField(max_length=4)
    tag_state = models.CharField(max_length=32)
    tag_no = models.CharField(max_length=12)
    nick_name = models.CharField(max_length=128)
    engine_type = models.CharField(max_length=32)
    mileage = models.DecimalField(max_digits=9, decimal_places=2)

# class Appointment(models.Model):
#     vehicle = models.ForeignKey(Vehicle, on_delete=models.CASCADE)
#     time = models.TimeField()
#     date = models.DateField()

class VehicleServiceNotification(models.Model):
    vehicle = models.ForeignKey(Vehicle, on_delete=models.CASCADE)
    reminder_interval_in_miles = models.IntegerField()
    reminder_interval_value = models.IntegerField()
    reminder_interval_units = models.CharField(max_length=25)
    last_mileage_serviced = models.DecimalField(max_digits=9, decimal_places=2)
