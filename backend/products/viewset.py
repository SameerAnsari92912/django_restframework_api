from rest_framework import viewsets,mixins


from .models import Product
from .serializers import ProductSerializers


class ProductViewSet(viewsets.ModelViewSet):
    '''
    
    
    '''
    queryset = Product.objects.all()
    serializer_class = ProductSerializers
    lookup_field = 'pk' # default


class ProductGenericViewSet(viewsets.GenericViewSet,
                            mixins.ListModelMixin,
                            mixins.RetrieveModelMixin,):
    """
    get -> list -> Queryset
    get -> retreive -> Product Instance Detail View
    
    """
    queryset = Product.objects.all()
    serializer_class = ProductSerializers
    lookup_field = 'pk' # default