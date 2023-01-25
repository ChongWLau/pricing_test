from django.db import models
from django.core.validators import MinValueValidator, MaxValueValidator

from dashboard.constants import TEST_GROUP, MARTIAL_STATUS

from datetime import datetime

# Create your models here.
class Quotes(models.Model):
    
    id = models.BigAutoField(primary_key=True)
    transaction_date = models.DateField(default=datetime(1970,1,1))
    test_group = models.CharField(
        max_length=1, choices=TEST_GROUP, default='A'
    )
    sale_indicator = models.BooleanField(default=False)
    net_price = models.DecimalField(max_digits=12, decimal_places=8, null=True)
    profit = models.DecimalField(max_digits=12, decimal_places=8, null=True)
    tax = models.DecimalField(max_digits=12, decimal_places=8, null=True)
    total_price = models.DecimalField(max_digits=12, decimal_places=8, null=True)
    customer_age = models.PositiveSmallIntegerField(
        validators=[MinValueValidator(1), MaxValueValidator(100)], null=True
    )
    licence_length = models.DecimalField(max_digits=12, decimal_places=8, null=True)
    marital_status = models.CharField(
        max_length=1, choices=MARTIAL_STATUS, null=True
    )
    credit_score = models.DecimalField(max_digits=12, decimal_places=8, null=True)
    vehicle_value = models.PositiveIntegerField(null=True)
    vehicle_mileage = models.PositiveIntegerField(null=True)
