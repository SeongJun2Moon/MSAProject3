from django.http import JsonResponse
from rest_framework.authtoken.models import Token
from rest_framework.decorators import api_view, parser_classes
from rest_framework.parsers import JSONParser

from rest_framework.response import Response
from movies.theater.repositories import TheatersRepository
from movies.theater.serializers import TheatersSerializer


@api_view(['POST', 'GET', 'PUT', 'PATCH','DELETE'])
@parser_classes([JSONParser])
def theater(request):
    if request.method == "POST":
        return TheatersSerializer().create(request.data)
    elif request.method == "GET":
        return TheatersSerializer().find_by_id(request.data)
    elif request.method == "PUT":
        return TheatersSerializer().update(request.data)
    elif request.method == "PATCH":
        return None
    elif request.method == "DELETE":
        return TheatersSerializer().delete(request.data)


@api_view(['GET'])
@parser_classes([JSONParser])
def theater_list(request):  return TheatersRepository().get_all(request.data)