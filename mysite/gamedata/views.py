from django.shortcuts import render
from django.http import HttpResponse, Http404, JsonResponse, HttpResponseNotFound
from rest_framework.parsers import JSONParser
from django.views.decorators.csrf import csrf_exempt
from .models import GameInfo, add_new_titles, add_new_titles_rawg, GameSubmissions
from .serializers import GameInfoContainerSerializer, GameSubmissionSerializer
from .responses import InvalidResponse, CustomResponse
from utils.igdb import Credentials, SearchType
from utils.rawg import RawgSearch
from utils.helpers import filter_array_json
from django.db.utils import IntegrityError


# Create your views here.

@csrf_exempt
def search(request):
    if request.method == 'GET':
        game_name = request.GET.get('name', None)

        # IGDB API - No longer used
        # api = SearchType()
        # api.set_search(game_name)
        # api.add_field('name')
        # api.add_where('rating > 0')
        # print(api)
        # results = Credentials.request(api)
        # print(results)

        # RAWG API
        rawg = RawgSearch()
        rawg.set_search(game_name)
        rawg.set_length(10)
        results = rawg.request()

        # Add Id's if games are missing
        add_new_titles_rawg(results)

        # Get ResultSet
        array = filter_array_json('id', results)
        # rs = {'data': GameInfo.objects.filter(igdblink__igdb_id__in=array)}
        rs = {'data': GameInfo.objects.filter(rawglink__rawg_id__in=array)}

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
            cer = CustomResponse()
            try:
                game_sub = GameSubmissions(game=GameInfo(id=sub.data['game']),
                                           time=sub.data['time'],
                                           difficulty=sub.data['difficulty'])
                game_sub.save()
                cer.read_response('success')
                return cer.create_response()

            except IntegrityError:
                # The pk for the game_id does not exist. Avoid making this occur
                cer.read_response('does_not_exist', attribute='Game')
                return cer.create_response()
        else:
            # Validation Failed
            resp = InvalidResponse()
            resp.read_error(sub.errors)
            return resp.create_response()
    else:
        return HttpResponseNotFound('<h1> Page not found <h1>')
