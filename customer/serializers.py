from rest_framework import serializers
from customer.models import Customer, Payment, Vehicle, VehicleServiceNotification

class CustomerSerializer(serializers.ModelSerializer):
    class Meta:
        model = Customer
        fields = '__all__'

class PaymentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Payment
        fields = '__all__'

class VehicleSerializer(serializers.ModelSerializer):
    class Meta:
        model = Vehicle
        fields = '__all__'

class VehicleServiceNotificationSerializer(serializers.ModelSerializer):
    class Meta:
        model = VehicleServiceNotification
        fields = '__all__'
