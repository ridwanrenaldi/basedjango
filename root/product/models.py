from django.db import models
from category.models import Category

class Product(models.Model):
  product_id = models.BigAutoField(primary_key=True)
  category = models.ForeignKey(Category, on_delete=models.CASCADE, null=True)
  product_name = models.CharField(max_length=100, null=True)
  product_description = models.TextField(null=True)
  product_stock = models.IntegerField(null=True)
  product_image = models.ImageField(upload_to='product/', null=True)
  product_created = models.DateTimeField(null=True, auto_now_add=True)
  product_modified = models.DateTimeField(null=True, auto_now=True)

  def __str__(self):
    return self.product_name
