from django.http import JsonResponse
from rest_framework.response import Response

from blog.tags.models import Tags
from blog.tags.serializers import TagsSerializer


class TagsRepository(object):

    def __init__(self):
        pass

    def get_all(self):
            return Response(TagsSerializer(Tags.objects.all(), many=True).data)

    def find_by_id(self):
            return Response(TagsSerializer(Tags.objects.all(), many=True).data)