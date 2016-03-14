from django.shortcuts import render
from django.http import HttpResponse, Http404

from .models import Category, Subcategory


def index(request):
    categories = Category.objects.order_by('-pub_date')
    return render(request, 'dashboard/dashboard.html', {'categories': categories})


def subcategory(request, subcategory_id):
    try:
        subcategory = Subcategory.objects.get(pk=subcategory_id)
    except Subcategory.DoesNotExist:
        raise Http404('Subcategory does not exist!')
    return render(request, 'dashboard/subcategory.html', {'subcategory': subcategory})
