from rest_framework import serializers
from films.models import *

class FilmlistSerializers(serializers.ModelSerializer):
    class Meta:
        model = Film
        fields = ['id', 'image', 'name_rus', 'name_en', 'name_tk', 'genre_ru', 'genre_en', 'genre_tk', 'sssr_or_not']

class ActorlistSerializers(serializers.ModelSerializer):
    class Meta:
        model = Actors
        fields = ['id', 'name_eng', 'name_rus', 'name_tkm', 'surname_eng', 'surname_rus', 'surname_tkm', 'father_name_eng', 'father_name_rus', 'father_name_tkm', 'image']

class ActordetaileSerializers(serializers.ModelSerializer):
    films = FilmlistSerializers(many=True, read_only=True)
    class Meta:
        model = Actors
        fields = '__all__'

class ScreenwriterlistSerializers(serializers.ModelSerializer):
    class Meta:
        model = Screenwriter
        fields = ['id', 'name_eng', 'name_rus', 'name_tkm', 'surname_eng', 'surname_rus', 'surname_tkm', 'father_name_eng', 'father_name_rus', 'father_name_tkm', 'image']

class ScreenwriterdetaileSerializers(serializers.ModelSerializer):
    films = FilmlistSerializers(many=True, read_only=True)
    class Meta:
        model = Screenwriter
        fields = '__all__'

class DirectorlistSerializers(serializers.ModelSerializer):
    class Meta:
        model = Director
        fields = ['id', 'name_eng', 'name_rus', 'name_tkm', 'surname_eng', 'surname_rus', 'surname_tkm', 'father_name_eng', 'father_name_rus', 'father_name_tkm', 'image']


class DirectordetaileSerializers(serializers.ModelSerializer):
    films = FilmlistSerializers(many=True, read_only=True)
    class Meta:
        model = Director
        fields = '__all__'
    

class NewslistSerializers(serializers.ModelSerializer):
    class Meta:
        model = News
        fields = ['id', 'image', 'title_eng', 'title_rus', 'title_tkm', 'short_content_rus', 'short_content_eng', 'short_content_tkm', 'publication_date']

class NewsdetailSerializers(serializers.ModelSerializer):
    class Meta:
        model = News
        fields = ['id', 'title_eng', 'title_rus', 'title_tkm', 'content_rus', 'content_eng', 'content_tkm', 'publication_date']

class ImagehisSerializer(serializers.ModelSerializer):
    class Meta:
        model = Imagehistory
        fields = '__all__'

class ImagehisssrSerializer(serializers.ModelSerializer):
    class Meta:
        model = ImagehistorySSSR
        fields = '__all__'
class StudiohistorySerializers(serializers.ModelSerializer):
    imagehistory = ImagehisSerializer(many=True,read_only=True)
    class Meta:
        model = StudioHistory
        fields = '__all__'

class CreatorSerializers(serializers.ModelSerializer):
    class Meta:
        model = StudioHistory
        fields = ['creator_bio_rus', 'creator_bio_eng', 'creator_bio_tkm', 'creator_birth_date']

class FilmdetailSerializers(serializers.ModelSerializer):
    screenwriter = ScreenwriterlistSerializers(many=True,read_only=True) 
    actors = ActorlistSerializers(many=True, read_only=True)
    director = DirectorlistSerializers(many=True,read_only=True) 
    
    class Meta:
        model = Film
        fields = '__all__'

class TrailorSerializers(serializers.ModelSerializer):
    class Meta:
        model = Trailer
        fields = ['video']

class TrailordetailSerializers(serializers.ModelSerializer):
    class Meta:
        model = Trailer
        fields = ['video']

class StudiohistorySSSRSerializers(serializers.ModelSerializer):
    creator_bio_rus = serializers.SerializerMethodField()
    creator_bio_eng = serializers.SerializerMethodField()
    creator_bio_tkm = serializers.SerializerMethodField()
    creator_birth_date = serializers.SerializerMethodField()
    imagehistorysssr = ImagehisssrSerializer(many=True,read_only=True)
    class Meta:
        model = StudioHistorySSSR
        fields = '__all__'

    def get_creator_bio_rus(self, obj):
        studio_history = StudioHistory.objects.first()
        return studio_history.creator_bio_rus if studio_history else None

    def get_creator_bio_eng(self, obj):
        studio_history = StudioHistory.objects.first()
        return studio_history.creator_bio_eng if studio_history else None

    def get_creator_bio_tkm(self, obj):
        studio_history = StudioHistory.objects.first()
        return studio_history.creator_bio_tkm if studio_history else None
    
    def get_creator_birth_date(self, obj):
        studio_history = StudioHistory.objects.first()
        return studio_history.creator_birth_date if studio_history else None