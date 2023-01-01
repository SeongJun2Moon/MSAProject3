from django.http import JsonResponse
from rest_framework.response import Response

from blog.busers.models import Busers
from blog.busers.serializers import BusersSerializer


class BusersRepository(object):

    def __init__(self):
        pass

    def get_all(self):
            return Response(BusersSerializer(Busers.objects.all(), many=True).data)

    def find_by_id(self):
            return Response(BusersSerializer(Busers.objects.all(), many=True).data)