# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models

# Create your models here.
class Customer(models.Model):

    class Meta:

        db_table = 'customer'

    name = models.CharField(max_length=200)

    def __str__(self):
        return self.name

class Book(models.Model):

    class Meta:

        db_table = 'book'

    title = models.CharField(max_length=200)
    customer = models.ForeignKey(Customer, on_delete=models.CASCADE, null=True)
    status = models.IntegerField(default=1) # 0: emprestado; 1: disponível
    reservation_date = models.DateTimeField(null=True)

    def __str__(self):
        return self.title