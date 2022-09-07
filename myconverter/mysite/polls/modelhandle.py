# from django.db import models
# from model_utils.models import TimeStampedModel
# from django.conf import settings
from .models import  Fileupl, FilmWork, FileFilmWork
from .views import question_list
# print(FilmWork.objects.all())

def get_data_from_model(modelname):
    return FilmWork.objects.all()

if __name__ == '__main__':
    request = 'http://127.0.0.1:8000/polls/question/ question_text="print test"'
    request_2 = '"http://127.0.0.1:8000/polls/question/3/", json={'question_text': "New text"}'
    question_list(request)
