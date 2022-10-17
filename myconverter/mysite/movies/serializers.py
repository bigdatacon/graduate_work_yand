from .models import FilmWorkMovie
from rest_framework import serializers


class FilmWorkMovieSerializer(serializers.ModelSerializer):
    class Meta:
        model = FilmWorkMovie
        fields = ['id', 'title', 'description', 'rating', 'genres', 'persons']
