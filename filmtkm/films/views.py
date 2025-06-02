from rest_framework.response import Response
from rest_framework.decorators import api_view, APIView
from rest_framework import status
from films.models import *
from .serializers import *
from django.shortcuts import get_object_or_404
from rest_framework.generics import ListAPIView

class Imagehis(ListAPIView):
    queryset = Imagehistory.objects.all()
    serializer_class = ImagehisSerializer
class Trailorlist(ListAPIView):
    queryset = Trailer.objects.all()
    serializer_class = TrailorSerializers    
class Actorlist(ListAPIView):
    queryset = Actors.objects.all()
    serializer_class = ActorlistSerializers

class Filmlist(ListAPIView):
    queryset = Film.objects.all()
    serializer_class = FilmlistSerializers

class Screenwriterlist(ListAPIView):
    queryset = Screenwriter.objects.all()
    serializer_class = ScreenwriterlistSerializers

class Directorlist(ListAPIView):
    queryset = Director.objects.all()
    serializer_class = DirectorlistSerializers

class Newslist(ListAPIView):
    queryset = News.objects.all()
    serializer_class = NewslistSerializers

@api_view(['GET'])
def Directordetail(request, director_id):
    director = get_object_or_404(Director, id=director_id)
    serializer = DirectordetaileSerializers(director, context={'request': request})
    return Response(serializer.data)

@api_view(['GET'])
def Screenwriterdetail(request, screenwriter_id):
    screenwriter = get_object_or_404(Screenwriter, id=screenwriter_id)
    serializer = ScreenwriterdetaileSerializers(screenwriter, context={'request': request})
    return Response(serializer.data)

@api_view(['GET'])
def Actordetail(request, actor_id):
    actor = get_object_or_404(Actors, id=actor_id)
    serializer = ActordetaileSerializers(actor, context={'request': request})
    return Response(serializer.data)

@api_view(['GET'])
def Newsdetail(request, new_id):
    news = get_object_or_404(News, id=new_id)
    serializer = NewsdetailSerializers(news, context={'request': request})
    return Response(serializer.data)

@api_view(['GET'])
def Filmsdetail(request, film_id):
    films = get_object_or_404(Film, id=film_id)
    serializer = FilmdetailSerializers(films, context={'request': request})
    return Response(serializer.data)

@api_view(['GET'])
def Studiohistory(request):
    studiohistory = StudioHistory.objects.all() 
    serializer = StudiohistorySerializers(studiohistory, many=True, context={'request': request})
    return Response(serializer.data)

@api_view(['GET'])
def StudiohistorySSSR(request):
    studiohistorysssr = StudioHistorySSSR.objects.all() 
    serializer = StudiohistorySSSRSerializers(studiohistorysssr, many=True, context={'request': request})
    return Response(serializer.data)

@api_view(['GET'])
def Trailordetail(request, trailor_id):
    trailors = get_object_or_404(Trailer, id=trailor_id)
    serializer = TrailordetailSerializers(trailors, context={'request': request})
    return Response(serializer.data)
