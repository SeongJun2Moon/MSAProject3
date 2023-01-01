from django.http import JsonResponse
from rest_framework.authtoken.models import Token
from rest_framework.decorators import api_view, parser_classes
from rest_framework.parsers import JSONParser

from rest_framework.response import Response
from shop.products.repositories import ProductsRepository
from shop.products.serializers import ProductsSerializer


@api_view(['POST', 'GET', 'PUT', 'PATCH','DELETE'])
@parser_classes([JSONParser])
def products(request):
    if request.method == "POST":
        return ProductsSerializer().create(request.data)
    elif request.method == "GET":
        return ProductsSerializer().find_by_id(request.data)
    elif request.method == "PUT":
        return ProductsSerializer().update(request.data)
    elif request.method == "PATCH":
        return None
    elif request.method == "DELETE":
        return ProductsSerializer().delete(request.data)


@api_view(['GET'])
@parser_classes([JSONParser])
def products_list(request):  return ProductsRepository().get_all(request.data)