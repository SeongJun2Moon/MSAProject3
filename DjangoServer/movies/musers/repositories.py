from django.http import JsonResponse
from rest_framework.response import Response

from movies.musers.models import Musers
from movies.musers.serializers import MusersSerializer


class MusersRepository(object):

    def __init__(self):
        pass

    def get_all(self):
            return Response(MusersSerializer(Musers.objects.all(), many=True).data)

    def find_by_id(self):
            return Response(MusersSerializer(Musers.objects.all(), many=True).data)