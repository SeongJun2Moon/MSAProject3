from django.http import JsonResponse
from rest_framework.decorators import api_view, parser_classes
from rest_framework.parsers import JSONParser
from exrc.nlp.samsung_report.services import Controller


@api_view(['GET'])
@parser_classes([JSONParser])
def samsung(request):
    result = Controller().data_analysis()
    return JsonResponse({'result' : result})
