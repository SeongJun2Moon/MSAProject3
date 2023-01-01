from django.http import JsonResponse
from rest_framework.authtoken.models import Token
from rest_framework.decorators import api_view, parser_classes
from rest_framework.parsers import JSONParser

from rest_framework.response import Response
from shop.categories.repositories import CategoriesRepository
from shop.categories.serializers import CategoriesSerializer


@api_view(['POST', 'GET', 'PUT', 'PATCH','DELETE'])
@parser_classes([JSONParser])
def categories(request):
    if request.method == "POST":
        return CategoriesSerializer().create(request.data)
    elif request.method == "GET":
        return CategoriesSerializer().find_by_id(request.data)
    elif request.method == "PUT":
        return CategoriesSerializer().update(request.data)
    elif request.method == "PATCH":
        return None
    elif request.method == "DELETE":
        return CategoriesSerializer().delete(request.data)


@api_view(['GET'])
@parser_classes([JSONParser])
def categories_list(request):  return CategoriesRepository().get_all(request.data)