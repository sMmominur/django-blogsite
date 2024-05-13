from django.shortcuts import render
from blog.services.category_service import CategoryService

def home_page(request):
    try:
        active_categories = CategoryService.get_active_categories()
    except Exception as e:
        print(f"Error occurred while fetching active categories: {e}")
        return render(request,'error/500.html')
    
    return render(request, 'home.html', {'active_categories': active_categories})
    
    
#top highlights
#Latest Articles
