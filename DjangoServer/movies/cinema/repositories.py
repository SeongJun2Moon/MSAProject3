from django.http import JsonResponse
from rest_framework.response import Response

from movies.cinema.models import Cinema
from movies.cinema.serializers import CinemaSerializer


class CinemaRepository(object):

    def __init__(self):
        pass

    def get_all(self):
            return Response(CinemaSerializer(Cinema.objects.all(), many=True).data)

    def find_by_id(self):
            return Response(CinemaSerializer(Cinema.objects.all(), many=True).data)