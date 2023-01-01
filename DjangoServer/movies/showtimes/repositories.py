from django.http import JsonResponse
from rest_framework.response import Response

from movies.showtimes.models import Showtimes
from movies.showtimes.serializers import ShowtimesSerializer


class ShowtimesRepository(object):

    def __init__(self):
        pass

    def get_all(self):
            return Response(ShowtimesSerializer(Showtimes.objects.all(), many=True).data)

    def find_by_id(self):
            return Response(ShowtimesSerializer(Showtimes.objects.all(), many=True).data)