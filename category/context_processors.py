from category.models import MainCategory
from store.models import Product


def cates(request):
    maincat = MainCategory.objects.all()
    products   = Product.objects.all().filter(is_available=True)
    return{'main_cat':maincat,'products':products}