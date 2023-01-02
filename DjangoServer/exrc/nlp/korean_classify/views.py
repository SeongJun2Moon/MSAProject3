from django.http import JsonResponse
from rest_framework.decorators import api_view, parser_classes
from rest_framework.parsers import JSONParser
from exrc.nlp.korean_classify.services import KoreanClassifyService
import json


@api_view(['POST'])
@parser_classes([JSONParser])
def koreanClassify(request):
    data = request.data
    print(f"******** 리액트에서 넘어온 데이터 : {data} ******** ")
    result = KoreanClassifyService().korean_classify(quiz=data['from'], answer=data['sentence'])
    print(f'국적결과: {result}')
    return JsonResponse({'result': result})