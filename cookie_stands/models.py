from random import random, randint

from django.contrib.auth import get_user_model
from django.db import models


class CookieStand(models.Model):
    location = models.CharField(max_length=256)
    owner = models.ForeignKey(
        get_user_model(), on_delete=models.CASCADE, null=True, blank=True
    )
    description = models.TextField(blank=True)
    hourly_sales = models.JSONField(default=list, null=True)
    minimum_customers_per_hour = models.IntegerField(default=0)
    maximum_customers_per_hour = models.IntegerField(default=0)
    average_cookies_per_sale = models.FloatField(default=0)
    hours = models.JSONField(default=list, blank=True)
    customersPerHour = models.JSONField(default=list, blank=False)
    totalCookies = models.JSONField(null=True, default=list, blank=True)





    # def save(self, *args, **kwargs):
    #     if not self.pk and not self.hourly_sales:
    #         min_ = self.minimum_customers_per_hour
    #         max_ = self.maximum_customers_per_hour
    #
    #         cookies_each_hour = [
    #             int(random.randint(min_, max_) * self.average_cookies_per_sale)
    #             for _ in range(14)
    #         ]
    #
    #         self.hourly_sales = cookies_each_hour
    #
    #     super().save(*args, **kwargs)
