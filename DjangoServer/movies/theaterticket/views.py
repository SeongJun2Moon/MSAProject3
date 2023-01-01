from django.http import JsonResponse
from rest_framework.authtoken.models import Token
from rest_framework.decorators import api_view, parser_classes
from rest_framework.parsers import JSONParser

from rest_framework.response import Response
from movies.theaterticket.repositories import TheaterticketRepository
from movies.theaterticket.serializers import TheaterTicketsSerializer


@api_view(['POST', 'GET', 'PUT', 'PATCH','DELETE'])
@parser_classes([JSONParser])
def theaterticket(request):
    if request.method == "POST":
        return TheaterTicketsSerializer().create(request.data)
    elif request.method == "GET":
        return TheaterTicketsSerializer().find_by_id(request.data)
    elif request.method == "PUT":
        return TheaterTicketsSerializer().update(request.data)
    elif request.method == "PATCH":
        return None
    elif request.method == "DELETE":
        return TheaterTicketsSerializer().delete(request.data)


@api_view(['GET'])
@parser_classes([JSONParser])
def theaterticket_list(request):  return TheaterticketRepository().get_all(request.data)