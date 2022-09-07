from .models import Fileupl, FilmWork, Question
from rest_framework import serializers

class QuestionSerializer(serializers.ModelSerializer):
    class Meta:
        model = Question
        fields = ['question_text', 'id', 'file_path']


class FileuplSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Fileupl
        fields = ['id', 'file_path', 'resolution', 'codec_name', 'film']

class FilmWorkSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = FilmWork
        fields = ['id', 'title', 'certificate', 'file_path']