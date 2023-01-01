from django.http import JsonResponse
from rest_framework.authtoken.models import Token
from rest_framework.decorators import api_view, parser_classes
from rest_framework.parsers import JSONParser

from rest_framework.response import Response
from movies.cinema.repositories import CinemaRepository
from movies.cinema.serializers import CinemasSerializer


@api_view(['POST', 'GET', 'PUT', 'PATCH','DELETE'])
@parser_classes([JSONParser])
def cinema(request):
    if request.method == "POST":
        return CinemasSerializer().create(request.data)
    elif request.method == "GET":
        return CinemasSerializer().find_by_id(request.data)
    elif request.method == "PUT":
        return CinemasSerializer().update(request.data)
    elif request.method == "PATCH":
        return None
    elif request.method == "DELETE":
        return CinemasSerializer().delete(request.data)


@api_view(['GET'])
@parser_classes([JSONParser])
def cinema_list(request):  return CinemaRepository().get_all(request.data)