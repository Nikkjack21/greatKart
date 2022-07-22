from django.db import models
from accounts.models import Account
from store.models import Product
# Create your models here.


class Cart(models.Model):
    user                = models.OneToOneField(Account, on_delete=models.CASCADE, blank=True)
    created_at          = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.user.username



class CartItem(models.Model):
    cart                = models.ForeignKey(Cart, on_delete=models.CASCADE, blank=True)
    product             = models.ForeignKey(Product, on_delete=models.CASCADE, blank=True)
    quantity            = models.IntegerField()
    is_active           = models.BooleanField(default=True)
    

    def __str__(self):
        return self.product.product_name

    def sub_total(self):
        return self.product.price * self.quantity

