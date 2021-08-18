from django.contrib import admin
from product.models import Product

class ProductAdmin(admin.ModelAdmin):
  list_display = ['product_id', 'category', 'product_name', 'product_description', 'product_created', 'product_modified']
  search_fields = ['product_id', 'category', 'product_name', 'product_description', 'product_created', 'product_modified']
  list_filter = ['product_id', 'category', 'product_name', 'product_description', 'product_created', 'product_modified']
  list_per_page = 5

admin.site.register(Product, ProductAdmin)