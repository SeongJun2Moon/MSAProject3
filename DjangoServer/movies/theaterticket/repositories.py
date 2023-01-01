from django.http import JsonResponse
from rest_framework.response import Response

from movies.theaterticket.models import Theater_tickets
from movies.theaterticket.serializers import TheaterTicketsSerializer


class TheaterticketRepository(object):

    def __init__(self):
        pass

    def get_all(self):
            return Response(TheaterTicketsSerializer(Theater_tickets.objects.all(), many=True).data)

    def find_by_id(self):
            return Response(TheaterTicketsSerializer(Theater_tickets.objects.all(), many=True).data)