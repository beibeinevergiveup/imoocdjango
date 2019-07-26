import json
from django.http import HttpResponse, JsonResponse
from thirdparty import juhe
from django.views import View
from utils.response import CommonResponseMixin, ReturnCode
from authorization.models import User
import utils


# def weather(request):
#     if request.method == 'GET':
#         city = request.GET.get('city')
#         data = []
#         result = juhe.weather(city)
#         result['city_info'] = city
#         data.append(result)
#         return JsonResponse(data=data, safe=False)
#     elif request.method == 'POST':
#         data = []
#         received_body = request.body.decode('utf-8')
#         received_body = json.loads(received_body)
#         print(received_body)
#         cities = received_body.get('cities')
#         for city in cities:
#             result = juhe.weather(city)
#             result['city_info'] = city
#             data.append(result)
#         return JsonResponse(data=data, safe=False)
#     pass


class weatherView(View, CommonResponseMixin):
    def get(self, request):
        if not utils.auth.already_authorized(request):
            response = self.wrap_json_response({}, code=ReturnCode.UNAUTHORIZED)
        else:
            data = []
            open_id = request.session.get('open_id')
            user = User.objects.filter(open_id=open_id)[0]
            cities = json.loads(user.focus_cities)
            for city in cities:
                result = juhe.weather(city.get('city'))
                result['city_info'] = city
                data.append(result)
            response = self.wrap_json_response(data = data, code=ReturnCode.SUCCESS)
            return JsonResponse(data=response, safe=False)
    pass

    def post(self, request):
        data = []
        received_body = request.body.decode('utf-8')
        received_body = json.loads(received_body)
        print(received_body)
        cities = received_body.get('cities')
        for city in cities:
            result = juhe.weather(city.get('city'))
            result['city_info'] = city
            data.append(result)
        response_data = self.wrap_json_response(data)
        return JsonResponse(data=response_data, safe=False)
        pass
