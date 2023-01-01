from django.http import JsonResponse
from rest_framework.response import Response

from blog.posts.models import Posts
from blog.posts.serializers import PostsSerializer


class PostsRepository(object):

    def __init__(self):
        pass

    def get_all(self):
            return Response(PostsSerializer(Posts.objects.all(), many=True).data)

    def find_by_id(self):
            return Response(PostsSerializer(Posts.objects.all(), many=True).data)