from django.http import JsonResponse
from rest_framework.authtoken.models import Token
from rest_framework.decorators import api_view, parser_classes
from rest_framework.parsers import JSONParser

from rest_framework.response import Response
from movies.musers.repositories import MusersRepository
from movies.musers.serializers import MusersSerializer


@api_view(['POST', 'GET', 'PUT', 'PATCH','DELETE'])
@parser_classes([JSONParser])
def musers(request):
    if request.method == "POST":
        return MusersSerializer().create(request.data)
    elif request.method == "GET":
        return MusersSerializer().find_by_id(request.data)
    elif request.method == "PUT":
        return MusersSerializer().update(request.data)
    elif request.method == "PATCH":
        return None
    elif request.method == "DELETE":
        return MusersSerializer().delete(request.data)


@api_view(['GET'])
@parser_classes([JSONParser])
def musers_list(request):  return MusersRepository().get_all(request.data)