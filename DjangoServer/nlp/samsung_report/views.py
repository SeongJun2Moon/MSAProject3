from django.http import JsonResponse
from rest_framework.decorators import api_view, parser_classes
from rest_framework.parsers import JSONParser
from nlp.samsung_report.services import Controller
import pandas as pd


@api_view(['GET'])
@parser_classes([JSONParser])
def samsung(request):
    result = Controller().data_analysis()
    return JsonResponse({'result' : result})
