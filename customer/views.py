from customer.models import Customer, Payment, Vehicle, VehicleServiceNotification
from customer.serializers import CustomerSerializer, PaymentSerializer
from customer.serializers import VehicleSerializer, VehicleServiceNotificationSerializer
from rest_framework import generics

# CUSTOMER
# Admin only
class CustomerList(generics.ListCreateAPIView):
    queryset = Customer.objects.all()
    serializer_class = CustomerSerializer

class CustomerDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Customer.objects.all()
    serializer_class = CustomerSerializer

# PAYMENT
# Retrieving payments for a given logged-in user
class UserPaymentList(generics.ListCreateAPIView):
    serializer_class = PaymentSerializer

    def get_queryset(self):
        user = self.request.user
        return Payment.objects.filter(account=user)

# Admin only
class PaymentList(generics.ListCreateAPIView):
    queryset = Payment.objects.all()
    serializer_class = PaymentSerializer

class PaymentDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Payment.objects.all()
    serializer_class = PaymentSerializer

# VEHICLE (user)
# Retrieving vehicles for a given logged-in user
class UserVehicleList(generics.ListCreateAPIView):
    serializer_class = VehicleSerializer

    def get_queryset(self):
        user = self.request.user
        return Vehicle.objects.filter(account=user)

# Admin only
class VehicleList(generics.ListCreateAPIView):
    queryset = Vehicle.objects.all()
    serializer_class = VehicleSerializer

class VehicleDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Vehicle.objects.all()
    serializer_class = VehicleSerializer

# SERVICE NOTIFICATION
# Retrieving vehicle service notifications for a given logged-in user
class UserVehicleServiceNotificationList(generics.ListCreateAPIView):
    serializer_class = VehicleServiceNotificationSerializer

    def get_queryset(self):
        user = self.request.user
        return VehicleServiceNotification.objects.filter(account=user)

# Admin only
class VehicleServiceNotificationList(generics.ListCreateAPIView):
    queryset = VehicleServiceNotification.objects.all()
    serializer_class = VehicleServiceNotificationSerializer

class VehicleServiceNotificationDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = VehicleServiceNotification.objects.all()
    serializer_class = VehicleServiceNotificationSerializer