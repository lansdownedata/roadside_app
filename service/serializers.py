from rest_framework import serializers
from service.models import Type, Issue, Ticket, Part, Review, CompanyCityService

class TypeSerializer(serializers.ModelSerializer):
    class Meta:
        model = Type
        fields = '__all__'

class IssueSerializer(serializers.ModelSerializer):
    class Meta:
        model = Issue
        fields = '__all__'

class TicketSerializer(serializers.ModelSerializer):
    class Meta:
        model = Ticket
        fields = '__all__'

class PartSerializer(serializers.ModelSerializer):
    class Meta:
        model = Part
        fields = '__all__'

class ReviewSerializer(serializers.ModelSerializer):
    class Meta:
        model = Review
        fields = '__all__'

class CompanyCityServiceSerializer(serializers.ModelSerializer):
    class Meta:
        model = CompanyCityService
        fields = '__all__'
