from django.shortcuts import render
from django.http import JsonResponse
from polls.models import FilmWork


def index(request):
    data = []
    for film in FilmWork.objects.all():
        film_info = {
            'uuid': film.id,
            'title': film.title,
            'certificate': film.certificate,
            'file_path': film.file_path.url,
            'files': []
        }
        for furl in film.files.all():
            film_info['files'].append(furl.file_path.url)
        data.append(film_info)
    return JsonResponse({'results': data})