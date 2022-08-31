from django.contrib import admin

from .models import Question, File, FilmWork, FileFilmWork, Choice

admin.site.register(Question)
admin.site.register(Choice)

admin.site.register(File)
admin.site.register(FilmWork)
admin.site.register(FileFilmWork)