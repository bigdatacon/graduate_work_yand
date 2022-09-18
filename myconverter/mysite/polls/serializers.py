from .models import Fileupl, FilmWork



class FileuplSerializer(serializers.ModelSerializer):
    class Meta:
        model = Fileupl
        fields = ['id', 'file_path', 'resolution', 'codec_name', 'film']

class FilmWorkSerializer(serializers.ModelSerializer):
    class Meta:
        model = FilmWork
        fields = ['id', 'title', 'certificate', 'file_path']