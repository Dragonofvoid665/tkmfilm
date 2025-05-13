from rest_framework import serializers
from .models import Actors, Film

class FilmSerializer(serializers.ModelSerializer):
    class Meta:
        model = Film
        fields = ['id', 'name_rus', 'name_eng', 'name_tkm', 'description_rus', 'description_eng', 'description_tkm', 'image_base64']

class ActorsSerializer(serializers.ModelSerializer):
    Films = FilmSerializer(many=True, read_only=True)  # Связанные фильмы

    class Meta:
        model = Actors
        fields = [
            'id', 'name_rus', 'name_eng', 'name_tkm', 'surname_rus', 'surname_eng', 'surname_tkm',
            'father_name_rus', 'father_name_eng', 'father_name_tkm', 'biography_rus',
            'biography_eng', 'biography_tkm', 'year', 'image_base64', 'Films'
        ]