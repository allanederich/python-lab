# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render
from rest_framework import generics
from .models import Customer,Book
from .serializers import CustomerSerializer,BookSerializer

# Create your views here.
class CustomerList(generics.ListCreateAPIView):

    queryset = Customer.objects.all()
    serializer_class = CustomerSerializer

class BookList(generics.ListCreateAPIView):

    queryset = Book.objects.all()
    serializer_class = BookSerializer