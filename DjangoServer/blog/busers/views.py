from django.http import JsonResponse
from rest_framework.decorators import api_view, parser_classes
from rest_framework.parsers import JSONParser
from rest_framework.authtoken.models import Token
from rest_framework.response import Response
from security.users.models import User
from blog.busers.service import UserService
from security.users.serializers import UserSerializer


# Create your views here.

@api_view(['POST'])
@parser_classes([JSONParser])
def login(request):
    try:
        print(f'로그인 정보: {request.data}')
        loginInfo = request.data
        loginUser = User.objects.get(user_email=loginInfo['email'])
        print(f"해당 email 을 가진 User: {loginInfo}")
        if loginUser["password"] == loginInfo["password"]:
            serializer = UserSerializer(loginUser, many=False)
            token = Token.objects.create(user=serializer)
            print(f"토큰값 : {token}")
            return JsonResponse(data=serializer.data, safe=False)
    except:
        return Response("LOGIN FAIL")

# @api_view(['GET'])
# @parser_classes([JSONParser])
# def users(request):
#     print(f" ##### GET at Here React ID is {request.GET['req']} and {request.GET}#####")
#     return JsonResponse({
#         'result': str(UserService().hook_react(int(request.GET['req'])))})