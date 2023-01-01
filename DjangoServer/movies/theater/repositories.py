from django.http import JsonResponse
from rest_framework.response import Response

from movies.theater.models import Theaters
from movies.theater.serializers import TheatersSerializer


class TheatersRepository(object):

    def __init__(self):
        pass

    def get_all(self):
            return Response(TheatersSerializer(Theaters.objects.all(), many=True).data)

    def find_by_id(self):
            return Response(TheatersSerializer(Theaters.objects.all(), many=True).data)