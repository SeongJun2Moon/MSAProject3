from django.http import JsonResponse
from rest_framework.authtoken.models import Token
from rest_framework.decorators import api_view, parser_classes
from rest_framework.parsers import JSONParser

from rest_framework.response import Response
from blog.views.repositories import ViewsRepository
from blog.views.serializers import ViewsSerializer


@api_view(['POST', 'GET', 'PUT', 'PATCH','DELETE'])
@parser_classes([JSONParser])
def views(request):
    if request.method == "POST":
        return ViewsSerializer().create(request.data)
    elif request.method == "GET":
        return ViewsSerializer().find_by_id(request.data)
    elif request.method == "PUT":
        return ViewsSerializer().update(request.data)
    elif request.method == "PATCH":
        return None
    elif request.method == "DELETE":
        return ViewsSerializer().delete(request.data)


@api_view(['GET'])
@parser_classes([JSONParser])
def views_list(request):  return ViewsRepository().get_all(request.data)