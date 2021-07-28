from django.shortcuts import render
from django.http import HttpResponse, Http404, JsonResponse, HttpResponseNotFound
from rest_framework.parsers import JSONParser
from django.views.decorators.csrf import csrf_exempt
from .models import GameInfo, add_new_titles
from .serializers import GameInfoContainerSerializer, IgdbContainerSerializer
from utils.igdb import Credentials, SearchType
from utils.helpers import filter_array_json


# Create your views here.

@csrf_exempt
def index(request):
    if request.method == 'GET':
        game_name = request.GET.get('name', None)

        # IGDB API
        api = SearchType()
        api.set_search(game_name)
        api.add_field('name')
        results = Credentials.request(api)

        # Add Id's if games are missing
        add_new_titles(results)

        # Create and Return HttpResponse
        array = filter_array_json('id', results)
        rs = {'data': GameInfo.objects.filter(igdblink__igdb_id__in=array)}
        serial = GameInfoContainerSerializer(rs)
        return JsonResponse(serial.data)
    else:
        return HttpResponseNotFound('<h1> Page not found <h1>')


@csrf_exempt
def submit(request):
    if request.method == 'POST':
        data = JSONParser().parse(request)
        print(data)
        return HttpResponse('Worked')
    else:
        return HttpResponseNotFound('<h1> Page not found <h1>')
