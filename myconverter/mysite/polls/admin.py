from django.contrib import admin

from .models import Question, File, FilmWork, FileFilmWork

admin.site.register(Question)

admin.site.register(File)
admin.site.register(FilmWork)
admin.site.register(FileFilmWork)