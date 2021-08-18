from django.contrib import admin
from category.models import Category

class CategoryAdmin(admin.ModelAdmin):
  list_display = ['category_id', 'category_name', 'category_description']
  search_fields = ['category_id', 'category_name', 'category_description']
  list_filter = ['category_id', 'category_name', 'category_description']
  list_per_page = 5

admin.site.register(Category, CategoryAdmin)
