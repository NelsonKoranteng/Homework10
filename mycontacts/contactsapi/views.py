from django.shortcuts import render
from rest_framework import viewsets
from .serializers import ContactSerializer
from .models import Contact
from rest_framework import viewsets, filters

class ContactViewSet(viewsets.ModelViewSet):
    queryset = Contact.objects.all()
    serializer_class = ContactSerializer
    filter_backends = [filters.OrderingFilter]
    ordering_fields = ['first_name', 'last_name']  # Fields that can be ordered
    ordering = ['last_name']  # Default ordering

# Create your views here.
