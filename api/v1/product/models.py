from django.db import models
from api.v1.base.models import BaseModel

# Create your models here.

class ProductCategory(BaseModel):
    description = models.CharField(max_length=100,null=False,blank=False,verbose_name='Descripción de la categoría')

    def __str__(self):
        return self.description

    class Meta:
        verbose_name = 'Categoría de producto'
        verbose_name_plural = 'Categorías de productos'
        db_table = 'product_category'

class Product(BaseModel):
    name = models.CharField(max_length=100,null=False,blank=False,verbose_name='Nombre del producto')
    description = models.CharField(max_length=100,null=False,blank=False,verbose_name='Descripción del producto')
    price = models.IntegerField(verbose_name='Precio del producto')
    stock = models.IntegerField(verbose_name='Stock')
    category = models.ForeignKey(ProductCategory, on_delete = models.CASCADE, verbose_name = 'Categoría')
    image = models.ImageField('Imagen ', upload_to='products/', default='', max_length=255, null=True, blank = True)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'Producto'
        verbose_name_plural = 'Productos'
        db_table = 'product'