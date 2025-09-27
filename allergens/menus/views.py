from django.shortcuts import render, get_object_or_404
from .models import Menu_Type, Category, Dish, Allergen # Ensure all models are imported

# Create your views here.
def index(request):
    """
    Renders the home page, showing all available Menu Types (e.g., 'Dinner', 'Lunch').
    """
    menu_types = Menu_Type.objects.all()
    context = {
        'menu_types': menu_types,
        'page_title': 'Welcome to Our Menu',
    }
    return render(request, 'menus/index.html', context)


def menu_detail(request, menu_type_slug):
    """
    Renders a specific Menu Type page, listing all its Categories and Dishes.
    """
    menu_type = get_object_or_404(Menu_Type, slug=menu_type_slug)
    # Get all distinct Categories associated with dishes in this menu type
    categories = Category.objects.filter(dish__menu_type=menu_type).distinct()
    dishes = Dish.objects.filter(menu_type=menu_type)
    
    context = {
        'menu_type': menu_type,
        'categories': categories,
        'dishes': dishes,
        'page_title': f'{menu_type.name} Menu',
    }
    return render(request, 'menus/menu_detail.html', context)


def category_detail(request, category_slug):
    """
    Renders a specific Category page, listing all Dishes within it.
    """
    category = get_object_or_404(Category, slug=category_slug)
    # Get dishes filtered by the current category
    dishes = Dish.objects.filter(category=category)
    
    context = {
        'category': category,
        'dishes': dishes,
        'page_title': f'{category.name}',
    }
    return render(request, 'menus/category_detail.html', context)


def dish_detail(request, dish_name):
    """
    Renders the detail page for a single Dish, showing its description and allergens.
    """
    # Note: This looks up the dish by its name (string) as defined in urls.py.
    dish = get_object_or_404(Dish, name=dish_name)
    allergens = dish.allergens.all() # Get all related allergens
    
    context = {
        'dish': dish,
        'allergens': allergens,
        'page_title': f'{dish.name} Details',
    }
    return render(request, 'menus/dish_detail.html', context)