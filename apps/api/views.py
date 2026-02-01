from django.forms import model_to_dict
from rest_framework.response import Response
from rest_framework.decorators import api_view

from apps.product.models import Product
from apps.product.serializers import ProductSerializer

@api_view(["GET" , "POST"])
def api_home(request, *args, **kwargs):
    """
    DRF API View
    """
    instance = Product.objects.all().order_by("?").first()
    data = {}
    if instance:
        # data = model_to_dict(model_data, fields=['__all__'])
        data = ProductSerializer(instance).data
        return Response(data)