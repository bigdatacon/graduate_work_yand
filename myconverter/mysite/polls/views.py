from django.shortcuts import render
from django.http import JsonResponse, HttpResponse
from .models import FilmWork, Fileupl, Question
from rest_framework import viewsets
from rest_framework import permissions
from .serializers import FileuplSerializer, FilmWorkSerializer, QuestionSerializer

from django.views.decorators.csrf import csrf_exempt
from rest_framework.parsers import JSONParser

#http http://127.0.0.1:8000/polls/question/
#http http://127.0.0.1:8000/polls/question/2
#http --form POST http://127.0.0.1:8000/polls/question/ question_text="print test"

@csrf_exempt
def question_list(request):
    """
    List all code snippets, or create a new snippet.
    """
    if request.method == 'GET':
        question = Question.objects.all()
        serializer = QuestionSerializer(question, many=True)
        return JsonResponse(serializer.data, safe=False)

    elif request.method == 'POST':
        data = JSONParser().parse(request)
        serializer = QuestionSerializer(data=data)
        if serializer.is_valid():
            serializer.save()
            return JsonResponse(serializer.data, status=201)
        return JsonResponse(serializer.errors, status=400)



@csrf_exempt
def question_detail(request, pk):
    """
    Retrieve, update or delete a code snippet.
    """
    try:
        question = Question.objects.get(pk=pk)
    except Question.DoesNotExist:
        return HttpResponse(status=404)

    if request.method == 'GET':
        serializer = QuestionSerializer(question)
        return JsonResponse(serializer.data)

    elif request.method == 'PUT':
        data = JSONParser().parse(request)
        serializer = QuestionSerializer(question, data=data)
        if serializer.is_valid():
            serializer.save()
            return JsonResponse(serializer.data)
        return JsonResponse(serializer.errors, status=400)

    elif request.method == 'DELETE':
        question.delete()
        return HttpResponse(status=204)

#создаю класс на базе ViewSet чтобы можно было писать видео файлы
class QuestionViewSet(viewsets.ModelViewSet):
    model = Question
    queryset = Question.objects.all()
    serializer_class = QuestionSerializer
    permission_classes = [permissions.IsAuthenticated]

class FileuplViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows users to be viewed or edited.
    """
    queryset = Fileupl.objects.all()
    serializer_class = FileuplSerializer
    permission_classes = [permissions.IsAuthenticated]


class FilmWorkViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows users to be viewed or edited.
    """
    queryset = FilmWork.objects.all()
    serializer_class = FilmWorkSerializer
    permission_classes = [permissions.IsAuthenticated]


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