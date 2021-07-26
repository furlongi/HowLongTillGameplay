from django.shortcuts import render
from django.http import HttpResponse, Http404, JsonResponse, HttpResponseNotFound
from rest_framework.parsers import JSONParser
from django.views.decorators.csrf import csrf_exempt
from .models import GameInfo
from .serializers import GameInfoSerializer, IgdbSearchSerializer, IgdbContainerSerializer
from utils.igdb import Credentials, SearchType



# Create your views here.

@csrf_exempt
def index(request):
    if request.method == 'GET':
        game_name = request.GET.get('name', None)
        api = SearchType()
        api.set_search(game_name)
        api.add_field('name')
        results = Credentials.request(api)
        serial = IgdbContainerSerializer(results)
        return JsonResponse(serial.data)
    else:
        return HttpResponseNotFound('<h1> Page not found <h1>')
