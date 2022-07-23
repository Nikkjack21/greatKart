from django.db import models
from django.core.validators import MinValueValidator, MaxValueValidator
from django.forms import BooleanField

from accounts.models import Account

# Create your models here.
class Coupons(models.Model):
    code     = models.CharField(max_length=50, unique=True)
    valid_from     = models.DateTimeField()
    valid_to       = models.DateTimeField()
    discount       = models.IntegerField(validators=[MinValueValidator(0), MaxValueValidator(100)])
    active      = BooleanField()


    def __str__(self):
        return self.code

    def discount_amount(self, total):
        return self.disocunt/100*total


class CouponUsed(models.Model):
    user = models.ForeignKey(Account, on_delete=models.CASCADE)
    coupon = models.ForeignKey(Coupons, on_delete=models.CASCADE)

    def __str__(self):
        return self.user.username