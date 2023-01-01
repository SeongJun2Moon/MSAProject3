from django.http import JsonResponse
from rest_framework.response import Response

from shop.products.models import Products
from shop.products.serializers import ProductsSerializer


class ProductsRepository(object):

    def __init__(self):
        pass

    def get_all(self):
            return Response(ProductsSerializer(Products.objects.all(), many=True).data)

    def find_by_id(self):
            return Response(ProductsSerializer(Products.objects.all(), many=True).data)