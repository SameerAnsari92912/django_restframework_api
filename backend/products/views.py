from django.shortcuts import render
from rest_framework import generics,mixins
# Create your views here.
from rest_framework.decorators import api_view
from rest_framework.response import Response

from django.shortcuts import get_object_or_404

from api.mixins import (StaffEditorPermissionsMixin,
                        UserQuerySetMixin)
from .models import Product
from .serializers import ProductSerializers


class ProductCreateAPIView(
    StaffEditorPermissionsMixin,
    generics.CreateAPIView):
    queryset = Product.objects.all()
    serializer_class = ProductSerializers


    def perform_create(self,serializer):
        #serialzers.save(user=self.request.user)
        print(serializer.validated_data)
       
        #title = serializer.validated_data.get('title')
        
        title = serializer.validated_data.get('title')
        content = serializer.validated_data.get('content') or None

        if content is None:
            content = title
        serializer.save(content=content)
        #send a Django signal

product_create_view = ProductCreateAPIView.as_view()


class ProductDetailAPIView(generics.RetrieveAPIView,
                           StaffEditorPermissionsMixin):
    queryset = Product.objects.all()
    serializer_class = ProductSerializers
    # lookup_field = 'pk' ??

product_detail_view = ProductDetailAPIView.as_view()

class ProductDestroyAPIView(
    StaffEditorPermissionsMixin,
    generics.DestroyAPIView):
    queryset = Product.objects.all()
    serializer_class = ProductSerializers
    lookup_field = 'pk'
    def perform_destroy(self,instance):
        #instance
        super().perform_destroy(instance)

    #Lookup_fields = 'pk'
    #Products.objects 

product_delete_view = ProductDestroyAPIView.as_view()



class ProductUpdateAPIView(
    StaffEditorPermissionsMixin,
    generics.UpdateAPIView):
    queryset = Product.objects.all()
    serializer_class = ProductSerializers

    lookup_field = 'pk'
    def perform_update(self,serializer):
        instance = serializer.save()
        if not instance.content:
            instance.content = instance.title
    #Products.objects 

product_update_view = ProductUpdateAPIView.as_view()

class ProductListCreateAPIView(
    UserQuerySetMixin,
    StaffEditorPermissionsMixin,
    generics.ListCreateAPIView):
    queryset = Product.objects.all()
    serializer_class = ProductSerializers
    
    def perform_create(self,serializer):
        #serialzer.save(user=self.request.user)
        #print(serializer.validated_data)
       # email = serializer.validated_data.pop('email')
       # print(email)
        
        title = serializer.validated_data.get('title')
        content = serializer.validated_data.get('content') or None

        if content is None:
            content = title
        serializer.save(user=self.request.user,content=content)
        #send a Django signal

    # def get_queryset(self,*args,**kwargs):
    #     qs = super().get_queryset(*args, **kwargs)
    #     request = self.request
    #     user = request.user
    #     if not user.is_authenticated:
    #         return Product.objects.none()
    #     #print(request.user)
    #     return qs.filter(user=request.user)
        

product_list_create_view = ProductListCreateAPIView.as_view()


class ProductMixinView(
    StaffEditorPermissionsMixin,
    mixins.ListModelMixin,
                       mixins.CreateModelMixin,
                       mixins.RetrieveModelMixin,
                       generics.GenericAPIView):
    queryset = Product.objects.all()
    serializer_class = ProductSerializers
    lookup_field = 'pk'
    def get(self,request,*args,**kwargs):
        print(args,kwargs)
        pk=kwargs.get("pk")
        if pk is not None:
            return self.retrieve(request, *args,**kwargs)
        return self.list(request,*args,**kwargs)

    def post(self,request,*args,**kwargs): #Http ->Post
        return self.create(request,*args,**kwargs)
        
product_mixin_view = ProductMixinView.as_view()

@api_view(['GET','POST'])
def product_alt_view(request,pk=None,*args,**kwargs):

    method = request.method
    if method == "GET":
        if pk is not None:
            queryset = Product.objects.filter(pk=pk)

            obj = get_object_or_404(Product,pk=pk)
            data = ProductSerializers(obj,many=False).data
            return Response(data)
        
        #detail view
        #url_args ??
        # get request -> detail views
        #list view
        queryset = Product.objects.all()
        data = ProductSerializers(queryset, many=True).data
        return Response(data)

    if method == "POST":
        #create an item

        serializer = ProductSerializers(data = request.data)
        if serializer.is_valid(raise_exception=True):
            title = serializer.validated_data.get('title')
            content = serializer.validated_data.get('content') or None
            if content is None:
                content = title
            serializer.save(content=content)
            return Response(serializer.data)
        return Response({"invalid":"not good data"},status=400)

