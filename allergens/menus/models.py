from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class Allergen(models.Model):
    name = models.CharField(max_length=50)
    slug = models.SlugField(max_length=50, unique=True)
    icon = models.URLField(blank=True)

    def __str__(self):
        return self.name


class Menu_Type(models.Model):
    name = models.CharField(max_length=20, unique=True)
    slug = models.SlugField(max_length=20, unique=True)
    logo = models.URLField(blank=True, default="https://i.ibb.co/7QpKsCX/white-background.jpg")
    background_image = models.URLField(blank=True, default="https://i.ibb.co/7QpKsCX/white-background.jpg")
    
    def __str__(self):
        return self.name
    
class Category(models.Model):
    name = models.CharField(max_length=20, unique=True)
    slug = models.SlugField(max_length=20, unique=True)
    cat_image = models.URLField(blank=True, default="https://i.ibb.co/7QpKsCX/white-background.jpg")
    
    def __str__(self):
        return self.name

class Subcategory(models.Model):
    name = models.CharField(max_length=20, unique=True)
    slug = models.SlugField(max_length=20, unique=True)
    subcat_image = models.URLField(blank=True, default="https://i.ibb.co/7QpKsCX/white-background.jpg")
    category = models.ForeignKey(Category, null=True, blank=True, on_delete=models.CASCADE)

    def __str__(self):
        return self.name

class Dish(models.Model):
    name = models.CharField(max_length=50)
    menu_type = models.ForeignKey(Menu_Type, null=True, blank=True, on_delete=models.CASCADE)
    category = models.ForeignKey(Category, null=True, blank=True, on_delete=models.CASCADE)
    subcategory = models.ForeignKey(Subcategory, null=True, blank=True, on_delete=models.CASCADE)
    description = models.TextField(blank=True)
    allergens = models.ManyToManyField(Allergen, blank=True)
    image = models.URLField(blank=True, default="https://i.ibb.co/7QpKsCX/white-background.jpg")
    STATUS_CHOICES = (
        ('active', 'Active'),
        ('inactive', 'Inactive'),
        ('archive', 'Archive'),
    )
    status = models.CharField(max_length=10, choices=STATUS_CHOICES, default='inactive')

    class Meta:
        unique_together = ('name', 'menu_type', 'category', 'subcategory')
        ordering = ['name']

    def __str__(self):
        return self.name
    

