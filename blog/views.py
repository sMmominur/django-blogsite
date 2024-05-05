from django.shortcuts import render
from django.http import JsonResponse
from blog.services.category_service import CategoryService
from django.core import serializers

def home_page(request):
    try:
        active_categories = CategoryService.get_active_categories()
    except Exception as e:
        print(f"Error occurred while fetching active categories: {e}")
        return render(request,'error/500.html')
    
    return render(request, 'home.html', {'active_categories': active_categories})
    

def fetch_category(request):
    active_categories = CategoryService.get_active_categories()
    categories_json = serializers.serialize('json', active_categories)
    return JsonResponse(categories_json, safe=False)
    