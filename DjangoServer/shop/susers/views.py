from django.http import JsonResponse
from rest_framework.authtoken.models import Token
from rest_framework.decorators import api_view, parser_classes
from rest_framework.parsers import JSONParser

from rest_framework.response import Response
from shop.susers.repositories import SusersRepository
from shop.susers.serializers import SusersSerializer


@api_view(['POST', 'GET', 'PUT', 'PATCH','DELETE'])
@parser_classes([JSONParser])
def susers(request):
    if request.method == "POST":
        return SusersSerializer().create(request.data)
    elif request.method == "GET":
        return SusersSerializer().find_by_id(request.data)
    elif request.method == "PUT":
        return SusersSerializer().update(request.data)
    elif request.method == "PATCH":
        return None
    elif request.method == "DELETE":
        return SusersSerializer().delete(request.data)


@api_view(['GET'])
@parser_classes([JSONParser])
def susers_list(request):  return SusersRepository().get_all(request.data)