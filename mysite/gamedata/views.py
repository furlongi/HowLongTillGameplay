from django.shortcuts import render
from django.http import HttpResponse, Http404, JsonResponse, HttpResponseNotFound
from rest_framework.parsers import JSONParser
from django.views.decorators.csrf import csrf_exempt
from .models import GameInfo, add_new_titles, GameSubmissions
from .serializers import GameInfoContainerSerializer, IgdbContainerSerializer, GameSubmissionSerializer
from utils.igdb import Credentials, SearchType
from utils.helpers import filter_array_json


# Create your views here.

@csrf_exempt
def search(request):
    if request.method == 'GET':
        game_name = request.GET.get('name', None)

        # IGDB API
        api = SearchType()
        api.set_search(game_name)
        api.add_field('name')
        api.add_where('rating > 0')
        print(api)
        results = Credentials.request(api)
        print(results)

        # Add Id's if games are missing
        add_new_titles(results)

        # Get ResultSet
        array = filter_array_json('id', results)
        rs = {'data': GameInfo.objects.filter(igdblink__igdb_id__in=array)}

        # Create and Return HttpResponse
        serial = GameInfoContainerSerializer(rs)
        return JsonResponse(serial.data)
    else:
        return HttpResponseNotFound('<h1> Page not found <h1>')


@csrf_exempt
def submit(request):
    if request.method == 'POST':
        data = JSONParser().parse(request)
        sub = GameSubmissionSerializer(data=data)
        if sub.is_valid():
            sub.save()
            return HttpResponse('Worked')
        else:
            print(sub.errors)
            return HttpResponse('Failed')
    else:
        return HttpResponseNotFound('<h1> Page not found <h1>')
