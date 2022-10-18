from django.shortcuts import render
from django.http import JsonResponse, HttpResponse
from .models import FilmWorkMovie
from rest_framework import viewsets
from rest_framework import permissions
from .serializers import FilmWorkMovieSerializer

class FilmWorkMovieViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows users to be viewed or edited.
    """
    queryset = FilmWorkMovie.objects.all()
    serializer_class = FilmWorkMovieSerializer
    # permission_classes = [permissions.IsAuthenticated]

def index(request):
    return HttpResponse("Hello, world. You're at the movies index.")

def indexfull(request):
    data = []
    for film in FilmWorkMovie.objects.all():
        film_info = {
            'uuid': film.id,
            'title': film.title,
            'description': film.description,
            'rating': film.rating,
            'genres': film.genres,
            'persons': film.persons,
        }
        data.append(film_info)
    return JsonResponse({'results': data})