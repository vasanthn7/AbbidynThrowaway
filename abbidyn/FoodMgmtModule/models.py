# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models
from django.utils import timezone
# from django.contrib.auth.models import User
# Create your models here.

class Food(models.Model):

    food_id = models.CharField(max_length=100)
    cook_id = models.ForeignKey("User", on_delete=models.CASCADE, null=False)
    name = models.CharField(max_length=100)
    discription = models.TextField(blank=False)
    order_limir = models.IntegerField(blank=True,default=5)

    def __str__(self):
        return self.food_id
