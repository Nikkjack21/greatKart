from tabnanny import verbose
from unicodedata import category, name
from django.db import models


maincategory = (('MEN','MEN'),('WOMEN','WOMEN'),('KIDS','KIDS'))
class MainCategory(models.Model):
    
    name                    = models.CharField( choices=maincategory, default='MEN' ,max_length=20)

    
    class Meta:
        verbose_name        = 'main category'
        verbose_name_plural = 'Main Category'

    def __str__(self):
        return self.name


class Category(models.Model):
    main_cat                = models.ForeignKey(MainCategory, related_name='subcategory', on_delete=models.CASCADE, null=True)
    category_name           = models.CharField(max_length=50)
    description             = models.TextField(max_length=250)

    class Meta:
        verbose_name        = 'category'
        verbose_name_plural = 'categories'


    def __str__(self):
        return self.category_name



