from service.models import Type, Issue, Ticket, Part, Review, CompanyCityService
from service.serializers import TypeSerializer, IssueSerializer, TicketSerializer
from service.serializers import PartSerializer, ReviewSerializer, CompanyCityServiceSerializer
from rest_framework import generics

# TYPE
class TypeList(generics.ListCreateAPIView):
    queryset = Type.objects.all()
    serializer_class = TypeSerializer

class TypeDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Type.objects.all()
    serializer_class = TypeSerializer

# ISSUE
class IssueList(generics.ListCreateAPIView):
    queryset = Issue.objects.all()
    serializer_class = IssueSerializer

class IssueDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Issue.objects.all()
    serializer_class = IssueSerializer

# TICKET
# Retrieving tickets for a given logged-in user
class UserTicketList(generics.ListCreateAPIView):
    serializer_class = TicketSerializer

    def get_queryset(self):
        user = self.request.user
        return Ticket.objects.filter(customer=user)

# Admin only
class TicketList(generics.ListCreateAPIView):
    queryset = Ticket.objects.all()
    serializer_class = TicketSerializer

class TicketDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Ticket.objects.all()
    serializer_class = TicketSerializer

# PART
class PartList(generics.ListCreateAPIView):
    queryset = Part.objects.all()
    serializer_class = PartSerializer

class PartDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Part.objects.all()
    serializer_class = PartSerializer

# REVIEW
# Retrieving tickets for a given logged-in user
class UserReviewList(generics.ListCreateAPIView):
    serializer_class = ReviewSerializer

    def get_queryset(self):
        user = self.request.user
        return Review.objects.filter(customer=user)

# Admin only
class ReviewList(generics.ListCreateAPIView):
    queryset = Review.objects.all()
    serializer_class = ReviewSerializer

class ReviewDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Review.objects.all()
    serializer_class = ReviewSerializer

# COMPANY CITY SERVICE
class CompanyCityServiceList(generics.ListCreateAPIView):
    queryset = CompanyCityService.objects.all()
    serializer_class = CompanyCityServiceSerializer

class CompanyCityServiceDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = CompanyCityService.objects.all()
    serializer_class = CompanyCityServiceSerializer