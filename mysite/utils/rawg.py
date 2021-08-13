from configparser import RawConfigParser
import requests


class RawgSearch:

    url = "https://api.rawg.io/api/games?key=f8c75212b7734415aac6fea342e42948&search=xeno"

    def __init__(self):
        self._search = None
        self._page = None
        self._length = None

        token = RawConfigParser()
        token.read('../configs.ini')
        self._token = token.get('secrets', 'RAWG_API')

    def set_search(self, search):
        self._search = search

    def set_page(self, page):
        self._page = page

    def set_length(self, length):
        self._length = length

    def request(self):
        strbuild = [f"key={self._token}"]
        if self._search:
            strbuild.append(f"search={self._search}")
        if self._page:
            strbuild.append(f"page={self._page}")
        if self._length:
            strbuild.append(f"page_size={self._length}")

        response = requests.get(RawgSearch.url + "&".join(strbuild))
        result = response.json()
        print([r["name"] for r in result["results"]])
        return response
