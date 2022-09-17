from rest_framework import serializers
from vendor.models import City, CityZip, Company, CompanyLocation, Vehicle, Contact

class CitySerializer(serializers.ModelSerializer):
    class Meta:
        model = City
        fields = '__all__'

class CityZipSerializer(serializers.ModelSerializer):
    class Meta:
        model = CityZip
        fields = '__all__'

class CompanySerializer(serializers.ModelSerializer):
    class Meta:
        model = Company
        fields = '__all__'

class CompanyLocationSerializer(serializers.ModelSerializer):
    class Meta:
        model = CompanyLocation
        fields = '__all__'

class VehicleSerializer(serializers.ModelSerializer):
    class Meta:
        model = Vehicle
        fields = '__all__'

class ContactSerializer(serializers.ModelSerializer):
    class Meta:
        model = Contact
        fields = '__all__'
