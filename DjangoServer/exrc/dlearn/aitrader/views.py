from django.http import JsonResponse
from rest_framework.decorators import api_view, parser_classes
from rest_framework.parsers import JSONParser
import tensorflow as tf

from exrc.dlearn.aitrader.models import SamsungKospi

@api_view(["GET"])
@parser_classes([JSONParser])
def aitrader(request):
    data = request.GET
    print(data['id'])
    return JsonResponse({"result": "hi"})


    # body = request.body
    # data = json.loads(body)
    # print(request.headers)
    # print(request.content_type)
    # print(f"### React ID is {data} ###")
    # resp = FashionService().service_model()(int(data['id']))
    # return JsonResponse({'result':resp})

