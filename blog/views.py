from django.shortcuts import render
from django.http import HttpResponse,HttpResponseNotFound,HttpResponseServerError
import datetime
from .models import Category
# Create your views here.
def home_page(request):
    return render(request,'home.html')
    #return HttpResponseNotFound(render(request,'../error/404.html'))
def show_404_error_page(request):
    return render(request, 'error/404.html')

def show_500_error_page(request):
    return render(request,'error/500.html')

   
    