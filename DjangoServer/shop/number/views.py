import json

from django.http import JsonResponse
from rest_framework.decorators import api_view, parser_classes
from rest_framework.parsers import JSONParser
import tensorflow as tf
from shop.number.service import NumberService


# Create your views here.

@api_view(['GET', 'POST'])
@parser_classes([JSONParser])
def number(request):
    if request.method == 'GET':
        print(f" ##### GET at Here React ID is {request.GET['req']} and {request.GET}#####")
        return JsonResponse({
            'result': str(NumberService().service_model(int(request.GET['req'])))})
    elif request.method == 'POST':
        data = json.loads(request.body)
        result = NumberService().service_model(int(data['Num']))
        return JsonResponse({'result': result})
    else: print(';;;;')
