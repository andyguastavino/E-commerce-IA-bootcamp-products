from django.contrib import admin
from .models import Section, Category, Subcategory, Product

# Register your models here.

admin.site.register(Section)
admin.site.register(Category)
admin.site.register(Subcategory)
admin.site.register(Product)