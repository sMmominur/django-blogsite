from django.urls import path
from .views import home_page, fetch_category

urlpatterns = [
    path('', home_page, name='blog'),  
    path('categories/', fetch_category, name='categories'),
]
