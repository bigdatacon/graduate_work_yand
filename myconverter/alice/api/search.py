"""Implements connector to Movie Async API for search info about movies, people, genres."""

from http import HTTPStatus
from typing import List, Optional, Tuple
from uuid import UUID
import requests



class SearchConnector:
    def __init__(self, url):
        self._url = url

    def _get_response(self, path: str, query: Optional[dict] = None) -> Optional[dict]:
        response = requests.get(self._url + path, params=query)
        return response

    def find_film_data(self, search_str: str) -> Optional[str]:
        film_uuid = self._find_film_uuid(search_str)
        film = self._get_film_by_uuid(film_uuid)
        return film

