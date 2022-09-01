from django.contrib import admin
# File, FilmWork, FileFilmWork,
from .models import Question,  Choice, Fileupl, FilmWork, FileFilmWork

admin.site.register(Question)
admin.site.register(Choice)

# admin.site.register(File)
admin.site.register(FilmWork)
admin.site.register(FileFilmWork)
admin.site.register(Fileupl)
