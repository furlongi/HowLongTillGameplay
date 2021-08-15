from configparser import RawConfigParser
import requests


class RawgSearch:

    url = "https://api.rawg.io/api/games?"

    def __init__(self):
        self._search = None
        self._page = None
        self._length = None
        self._sort = None

        token = RawConfigParser()
        token.read('../configs.ini')
        self._token = token.get('secrets', 'RAWG_API')

    def set_search(self, search):
        self._search = search

    def set_page(self, page):
        self._page = page

    def set_length(self, length):
        self._length = length

    def set_sort(self, sort):
        self._sort = sort

    def request(self):
        strbuild = [f"key={self._token}"]
        if self._search:
            strbuild.append(f"search={self._search}")
        if self._page:
            strbuild.append(f"page={self._page}")
        if self._length:
            strbuild.append(f"page_size={self._length}")
        if self._sort:
            strbuild.append(f"ordering={self._sort}")

        response = requests.get(RawgSearch.url + "&".join(strbuild))
        result = response.json()
        # print([r["name"] for r in result["results"]])
        return result["results"]
