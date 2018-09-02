# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models
from django.utils import timezone
# from django.contrib.auth.models import User
# Create your models here.

class Orders(models.Model):
    STATUS_CHOICES = {
        ("pending", "Pending"),
        ("completed", "Completed")
    }
    PAYMENT_CHOICES = {
        ("COD", "Cash_On_Delivery"),
        ("card", "Card"),
        ("net","Internet_Banking"),
    }
    food_id = models.ForeignKey("Food", on_delete=models.CASCADE, null=False)
    cook_id = models.ForeignKey("User", on_delete=models.CASCADE, null=False)
    delivery_address = models.TextField(blank=False)
    order_date = models.DateField(blank=False, default=None)
    order_time = models.TimeField(blank=False, default=None)
    status = models.CharField(max_length=10, choices=STATUS_CHOICES, default="pending")
    payment_mode = models.CharField(max_length=20, choices=PAYMENT_CHOICES, default="COD")
    deleted_on = models.DateField(default=None, null=True)



    class Meta:
        ordering = ["order_date" ,"order_time"]

    def __str__(self):
        return self.food_id
