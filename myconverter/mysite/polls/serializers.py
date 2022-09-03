from .models import Fileupl
from rest_framework import serializers

class FileuplSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Fileupl
        fields = ['id', 'file_path', 'resolution', 'codec_name', 'film']