from django.http import JsonResponse
from rest_framework.authtoken.models import Token
from rest_framework.decorators import api_view, parser_classes
from rest_framework.parsers import JSONParser

from rest_framework.response import Response
from blog.busers.repositories import BusersRepository
from blog.busers.serializers import BusersSerializer


@api_view(['POST', 'GET', 'PUT', 'PATCH','DELETE'])
@parser_classes([JSONParser])
def busers(request):
    if request.method == "POST":
        return BusersSerializer().create(request.data)
    elif request.method == "GET":
        return BusersRepository().find_by_id(request.data)
    elif request.method == "PUT":
        return BusersSerializer().update(request.data)
    elif request.method == "PATCH":
        return None
    elif request.method == "DELETE":
        return BusersSerializer().delete(request.data)


@api_view(['GET'])
@parser_classes([JSONParser])
def busers_list(request):  return BusersRepository().get_all(request.data)