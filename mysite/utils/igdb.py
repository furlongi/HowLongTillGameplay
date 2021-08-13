from configparser import RawConfigParser
from igdb.wrapper import IGDBWrapper
import json


class Credentials:

    @staticmethod
    def _get_token():
        token = RawConfigParser()
        token.read('../apiaccess.ini')
        return token.get('igdb', 'TOKEN')

    @staticmethod
    def _get_client():
        client = RawConfigParser()
        client.read('../configs.ini')
        return client.get('secrets', 'TWITCH_CLI')

    @staticmethod
    def request(search):

        access = Credentials._get_token()
        client = Credentials._get_client()

        wrapper = IGDBWrapper(client, access)
        return json.loads(wrapper.api_request('games', str(search)))


class SearchType:

    def __init__(self):
        self._search = None
        self._sort = None
        self._order = None
        self._where = []
        self._fields = []

    def set_search(self, search):
        self._search = search

    def set_sort(self, sort, order=None):
        self._sort = sort
        self._order = order

    def add_where(self, where):
        self._where.append(where)

    def add_where_list(self, where):
        self._where.extend(where)

    def add_field(self, field):
        self._fields.append(field)

    def add_field_list(self, field):
        self._fields.extend(field)

    def __str__(self):
        return ('' if self._search is None else f'search "{self._search}"; ') + \
               ('' if len(self._where) == 0 else f'where {" & ".join(self._where)}; ') + \
               ('' if len(self._fields) == 0 else f'fields {", ".join(self._fields)}; ') + \
               ('' if self._sort is None else f'sort {self._sort} {self._order if self._order else "DESC"}; ')
