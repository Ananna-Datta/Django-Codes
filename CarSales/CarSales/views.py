from django.shortcuts import render
from cars.models import Car,Brand
# from categories.models import Category



def home(request, brand_slug = None):
    data = Car.objects.all()
    if brand_slug is not None:
        brand = Brand.objects.get(slug = brand_slug)
        data = Car.objects.filter(category  = brand)
    # brand = Brand.objects.all()
    return render(request, 'home.html', {'data' : data})

