from django.contrib import admin
# File, FilmWork, FileFilmWork,
from .models import  Fileupl, FilmWork, FileFilmWork

class FileuplAdmin(admin.TabularInline):
    model = Fileupl

class FilmWorkAdmin(admin.ModelAdmin):
    list_display = ['title']
    inlines = [FileuplAdmin]

admin.site.register(FilmWork, FilmWorkAdmin)
admin.site.register(Fileupl)



# # admin.site.register(Question)
# # admin.site.register(Choice)
#
# # admin.site.register(File)
# admin.site.register(FilmWork)
admin.site.register(FileFilmWork)
# admin.site.register(Fileupl)
