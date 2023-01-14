from django.shortcuts import render
from django.http import HttpResponse
from django.core.exceptions import ObjectDoesNotExist
from django.db.models import Q, F

from store.models import Order

def say_hello(request):
    query_set = Order.objects.select_related('customer').prefetch_related('orderitem_set').order_by('-placed_at')[:5]
    return render(request,'hello.html',{'name':'Mohammadreza','products':list(query_set)}) 