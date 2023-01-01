from django.http import JsonResponse
from rest_framework.authtoken.models import Token
from rest_framework.decorators import api_view, parser_classes
from rest_framework.parsers import JSONParser

from rest_framework.response import Response
from blog.tags.repositories import TagsRepository
from blog.tags.serializers import TagsSerializer


@api_view(['POST', 'GET', 'PUT', 'PATCH','DELETE'])
@parser_classes([JSONParser])
def tags(request):
    if request.method == "POST":
        return TagsSerializer().create(request.data)
    elif request.method == "GET":
        return TagsSerializer().find_by_id(request.data)
    elif request.method == "PUT":
        return TagsSerializer().update(request.data)
    elif request.method == "PATCH":
        return None
    elif request.method == "DELETE":
        return TagsSerializer().delete(request.data)


@api_view(['GET'])
@parser_classes([JSONParser])
def tags_list(request):  return TagsRepository().get_all(request.data)