from datetime import timezone
from django.shortcuts import redirect, render
from .models import Coupons

from .forms import CouponApplyForm
# Create your views here.

def coupon_apply(request):
    now      = timezone.now()
    form  = CouponApplyForm(request.POST)
    if form.is_valid():
        code   = form.cleaned_data['code']
        try:
            coupon   = Coupons.objects.get(code__iexact=code,valid_from__lte=now,
                                                            valid_to__gte=now,active=True)

            request.session['coupon_id']= coupon.id
        except Coupons.DoesNotExist:
            request.session['coupon_id'] = None
        return redirect('cart')
