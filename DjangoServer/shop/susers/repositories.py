from django.http import JsonResponse
from rest_framework.response import Response

from shop.susers.models import Susers
from shop.susers.serializers import SusersSerializer


class SusersRepository(object):

    def __init__(self):
        pass

    def get_all(self):
            return Response(SusersSerializer(Susers.objects.all(), many=True).data)

    def find_by_id(self):
            return Response(SusersSerializer(Susers.objects.all(), many=True).data)