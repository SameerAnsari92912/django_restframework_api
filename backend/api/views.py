from django.shortcuts import render
from django.http import JsonResponse
from django.forms.models import model_to_dict
from rest_framework import serializers
#from django.http import JsonResponse , HttpResponse
import json 


from rest_framework.decorators import api_view
from rest_framework.response import Response


from products.models import Product
from products.serializers import ProductSerializers


# Create your views here.

@api_view(["POST"])
def api_home(request , *args , **kwargs):
    """
    DRF API View

    """
    #data = request.data
    
    #instance = Product.objects.all().order_by("?").first()
    #data = {}
    
    serializer = ProductSerializers(data = request.data)

    
    if serializer.is_valid(raise_exception = True):
        #data = model_to_dict(model_data, fields=['id','title','price','sale_price'])
        #data = ProductSerializers(instance).data
        #instance = serializer.save()
        print(serializer.data)
        return Response(serializer.data)
    
    return Response({"invalid":"not good data"}, status=400)
