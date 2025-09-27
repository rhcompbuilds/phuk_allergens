from django.contrib import admin
from .models import Allergen, Menu_Type, Category, Subcategory, Dish

# Register your models here.
admin.site.register(Allergen)
admin.site.register(Menu_Type)
admin.site.register(Category)
admin.site.register(Subcategory)
admin.site.register(Dish)