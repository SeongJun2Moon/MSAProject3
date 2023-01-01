from django.http import JsonResponse
from rest_framework.response import Response

from shop.carts.models import Carts
from shop.carts.serializers import CartsSerializer


class CartsRepository(object):

    def __init__(self):
        pass

    def get_all(self):
            return Response(CartsSerializer(Carts.objects.all(), many=True).data)

    def find_by_id(self):
            return Response(CartsSerializer(Carts.objects.all(), many=True).data)