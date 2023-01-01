from django.http import JsonResponse
from rest_framework.decorators import api_view, parser_classes
from rest_framework.parsers import JSONParser

from movies.movies.servieces import DcGan

from movies.movies.repositories import MovieRepository
from movies.movies.serializers import MovieSerializer

# Create your views here.

@api_view(['GET'])
@parser_classes([JSONParser])
def fake_faces(request):
    DcGan().show_image()
    print(f'Enter Show Faces with {request}')
    return JsonResponse({'Response Test ': 'SUCCEESS'})

@api_view(['POST', 'GET', 'PUT', 'PATCH','DELETE'])
@parser_classes([JSONParser])
def movie(request):
    if request.method == "POST":
        return MovieSerializer().create(request.data)
    elif request.method == "GET":
        return MovieSerializer().find_by_id(request.data)
    elif request.method == "PUT":
        return MovieSerializer().update(request.data)
    elif request.method == "PATCH":
        return None
    elif request.method == "DELETE":
        return MovieSerializer().delete(request.data)


@api_view(['GET'])
@parser_classes([JSONParser])
def movie_list(request):  return MovieRepository().get_all(request.data)