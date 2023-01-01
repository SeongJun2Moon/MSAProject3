from django.http import JsonResponse
from rest_framework.authtoken.models import Token
from rest_framework.decorators import api_view, parser_classes
from rest_framework.parsers import JSONParser

from rest_framework.response import Response
from shop.carts.repositories import CartsRepository
from shop.carts.serializers import CartsSerializer


@api_view(['POST', 'GET', 'PUT', 'PATCH','DELETE'])
@parser_classes([JSONParser])
def carts(request):
    if request.method == "POST":
        return CartsSerializer().create(request.data)
    elif request.method == "GET":
        return CartsSerializer().find_by_id(request.data)
    elif request.method == "PUT":
        return CartsSerializer().update(request.data)
    elif request.method == "PATCH":
        return None
    elif request.method == "DELETE":
        return CartsSerializer().delete(request.data)


@api_view(['GET'])
@parser_classes([JSONParser])
def carts_list(request):  return CartsRepository().get_all(request.data)