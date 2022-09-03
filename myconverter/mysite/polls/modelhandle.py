# from django.db import models
# from model_utils.models import TimeStampedModel
# from django.conf import settings
from .models import  Fileupl, FilmWork, FileFilmWork
# print(FilmWork.objects.all())

def get_data_from_model(modelname):
    return FilmWork.objects.all()