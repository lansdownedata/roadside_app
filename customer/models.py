from django.db import models

class Account(models.Model):
    first_name = models.CharField(max_length=96)
    last_name = models.CharField(max_length=96)
    email = models.CharField(max_length=96)
    main_phone = models.CharField(max_length=20)
    secondary_phone = models.CharField(max_length=20)
    main_account_holder_id = models.ForeignKey('self', on_delete=models.CASCADE)
    authorize_profile_id = models.IntegerField()
    created_on = models.DateTimeField(auto_now=True)

class Payment(models.Model):
    account = models.ForeignKey(Account, on_delete=models.CASCADE)
    authorize_payment_id = models.IntegerField()

class Vehicle(models.Model):
    owner_id = models.ForeignKey(Account, on_delete=models.CASCADE)
    driver_id = models.ForeignKey(Account, on_delete=models.CASCADE)
    make = models.CharField(max_length=64)
    model = models.CharField(max_length=64)
    color = models.CharField(max_length=32)
    year = models.CharField(max_length=4)
    tag_state = models.CharField(max_length=32)
    tag_no = models.CharField(max_length=12)
    nick_name = models.CharField(max_length=128)
    engine_type = models.CharField(max_length=32)
    mileage = models.DecimalField(max_digits=9, decimal_places=2)
