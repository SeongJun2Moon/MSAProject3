import json

from django.http import JsonResponse
from rest_framework.decorators import api_view, parser_classes
from rest_framework.parsers import JSONParser
import tensorflow as tf

from shop.fashion.fashion_service import FashionService

@api_view(['GET', "POST"])
@parser_classes([JSONParser])
def fashion(request):
    if request.method == "GET":
        data = request.GET
        print(f"리퀘스트 {data}")
        print(f"리퀘스트[id]타입 {type(data['id'])}")
        resp = FashionService().service_model(int(data['id']))
        return JsonResponse({"result": resp})
    elif request.method == "POST":
        req_data = request.data
        req_data_num = tf.constant(int(req_data["id2"]))
        print(f"리퀘스트 데이터 : {req_data}")
        print(f"리퀘스트 데이터 값: {req_data_num}")
        resp = FashionService().service_model(req_data_num)
        return JsonResponse({"result": resp})


    # body = request.body
    # data = json.loads(body)
    # print(request.headers)
    # print(request.content_type)
    # print(f"### React ID is {data} ###")
    # resp = FashionService().service_model()(int(data['id']))
    # return JsonResponse({'result':resp})

