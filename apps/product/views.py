from django.shortcuts import get_object_or_404
from rest_framework.response import Response
from rest_framework import generics
from rest_framework.decorators import api_view 

from .models import Product
from .serializers import ProductSerializer

class ProductDetailedAPIView(generics.RetrieveAPIView):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer
    # lookup_field = 'pk'

class ProductListCreateAPIView(generics.ListCreateAPIView):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer

    def perform_create(self, serializer):
        title = serializer.validated_data.get('title')
        content = serializer.validated_data.get('content') or None 
        if content is None:
            content = title
        serializer.save(content=content)
        

class ProductUpdateAPIView(generics.UpdateAPIView):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer
    # lookup_field = 'pk'
    
    # ! now it doesn't do pretty much
    def perform_update(self, serializer):
        instance = serializer.save()

class ProductDestroyAPIView(generics.DestroyAPIView):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer
    # lookup_field = 'pk'

# Just List method would be created, but can be shortcuted with ListCreate
# ! USING ListCreate Api View instead
# class ProductListAPIView(generics.ListAPIView):
#     queryset = Product.objects.all()
#     serializer_class = ProductSerializer







# !JUST FOR INFO HERE, FUNCTION BASED API VIES ARE TOO MASSY
@api_view(['GET' , 'POST'])
def product_alt_view(request, pk=None ,*args , **kwargs):
    method = request.method

    if method == "GET":
        if pk is not None:
            # get by id 
            obj = get_object_or_404(Product, pk=pk)
            data = ProductSerializer(obj, many=False).data
            return Response(data)
        # get list
        queryset = Product.objects.all()
        data = ProductSerializer(obj, many=True).data
        return Response(data)
    
    if method == "POST":
        # create method
        serializer = ProductSerializer(data=request.data)
        if serializer.is_valid(raise_exception=True):
            title = serializer.validated_data.get('title')
            content = serializer.validated_data.get('content') or None 
            if content is None:
                content = title
            serializer.save(content=content) 
            return Response(serializer.data)
        return Response({"invalid" : "not good data"}, status=400)