from django.shortcuts import render
from django.http import HttpResponse, Http404, JsonResponse, HttpResponseNotFound
from rest_framework.parsers import JSONParser
from django.views.decorators.csrf import csrf_exempt
from .models import GameInfo, IgdbLink
from .serializers import GameInfoSerializer, IgdbSearchSerializer, IgdbContainerSerializer
from utils.igdb import Credentials, SearchType
from django.db import transaction, IntegrityError



# Create your views here.

@csrf_exempt
def index(request):
    if request.method == 'GET':
        game_name = request.GET.get('name', None)
        api = SearchType()
        api.set_search(game_name)
        api.add_field('name')
        results = Credentials.request(api)
        test(results["data"])
        serial = IgdbContainerSerializer(results)
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


def test(array):
    """Test function to test feasibility"""
    print(array)
    ids = [entry["id"] for entry in array]
    result = {i.igdb_id for i in IgdbLink.objects.filter(pk__in=ids)}
    search = [entry for entry in array if entry["id"] not in result]
    info_entries = [GameInfo(name=entry['name']) for entry in search]

    with transaction.atomic():
        for i,e in enumerate(info_entries):
            e.save()
            new_id = GameInfo.objects.latest('id')
            obj = search[i]
            link = IgdbLink(igdb_id=obj['id'], game_id=new_id)
            link.save()
