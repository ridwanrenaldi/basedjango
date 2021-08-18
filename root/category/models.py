from django.db import models

class Category(models.Model):
  category_id = models.BigAutoField(primary_key=True)
  category_name = models.CharField(max_length=50, null=True)
  category_description = models.TextField(null=True)

  def __str__(self):
    return self.category_name
