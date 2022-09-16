from rest_framework import serializers
from customer.models import Customer, Payment, Vehicle, VehicleServiceNotification

class CustomerSerializer(serializers.Serializer):
    id = serializers.IntegerField(read_only=True)
    first_name = serializers.CharField(max_length=96)
    last_name = serializers.CharField(max_length=96)
    email = serializers.CharField(max_length=96)
    main_phone = serializers.CharField(max_length=20)
    secondary_phone = serializers.CharField(max_length=20)
    main_account_holder_id = serializers.IntegerField()
    created_on = serializers.DateTimeField(auto_now=True)

    def create(self, validate_data):
        """
        Create and return a new `Customer` instance, given the validated data.
        """
        return Customer.objects.create(**validate_data)

    def update(self, instance, validated_data):
        """
        Update and return an existing 'Customer' instance, given the validated data
        """
        instance.first_name = validated_data.get('first_name', instance.first_name)
        instance.last_name = validated_data.get('last_name', instance.last_name)
        instance.email = validated_data.get('email', instance.email)
        instance.main_phone = validated_data.get('main_phone', instance.main_phone)
        instance.secondary_phone = validated_data.get('secondary_phone', instance.secondary_phone)
        instance.save()
        return instance

class PaymentSerializer(serializers.Serializer):
    account = serializers.IntegerField()
    authorize_payment_id = serializers.IntegerField()

    def create(self, validate_data):
        """
        Create and return a new `Payment` instance, given the validated data.
        """
        return Payment.objects.create(**validate_data)

    def update(self, instance, validated_data):
        """
        Update and return an existing 'Payment' instance, given the validated data
        """
        instance.account = validated_data.get('account', instance.account)
        instance.authorize_payment_id = validated_data.get('authorize_payment_id', instance.authorize_payment_id)
        instance.save()
        return instance

class VehicleSerializer(serializers.Serializer):
    owner = serializers.IntegerField()
    driver = serializers.IntegerField()
    make = serializers.CharField(max_length=64)
    model = serializers.CharField(max_length=64)
    color = serializers.CharField(max_length=32)
    year = serializers.CharField(max_length=4)
    tag_state = serializers.CharField(max_length=32)
    tag_no = serializers.CharField(max_length=12)
    nick_name = serializers.CharField(max_length=128)
    engine_type = serializers.CharField(max_length=32)
    mileage = serializers.DecimalField(max_digits=9, decimal_places=2)

    def create(self, validate_data):
        """
        Create and return a new `Payment` instance, given the validated data.
        """
        return Vehicle.objects.create(**validate_data)

    def update(self, instance, validated_data):
        """
        Update and return an existing 'Payment' instance, given the validated data
        """
        instance.owner = validated_data.get('owner', instance.owner)
        instance.authorize_payment_id = validated_data.get('authorize_payment_id', instance.authorize_payment_id)
        instance.save()
        return instance

class VehicleServiceNotificationSerializer(serializers.Serializer):
    vehicle = serializers.IntegerField()
    reminder_interval_in_miles = serializers.IntegerField()
    reminder_interval_value = serializers.IntegerField()
    reminder_interval_units = serializers.CharField(max_length=25)
    last_mileage_serviced = serializers.DecimalField(max_digits=9, decimal_places=2)

    def create(self, instance, validate_data):
        """
        Create and return a new `Service Notification` instance, given the validated data.
        """
        return VehicleServiceNotification.objects.create(**validate_data)

    def update(self, instance, validated_data):
        """
        Update and return an existing 'Payment' instance, given the validated data
        """
        instance.vehicle = validated_data.get('vehicle', instance.vehicle)
        instance.reminder_interval_in_miles = validated_data.get('reminder_interval_in_miles', instance.reminder_interval_in_miles)
        instance.reminder_interval_value = validated_data.get('reminder_interval_value', instance.reminder_interval_value)
        instance.reminder_interval_units = validated_data.get('reminder_interval_units', instance.reminder_interval_units)
        instance.last_mileage_serviced = validated_data.get('last_mileage_serviced', instance.last_mileage_serviced)
