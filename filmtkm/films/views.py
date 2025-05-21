from rest_framework.response import Response
from rest_framework.decorators import api_view
from  films.models import *
from .serializers import *
from django.shortcuts import get_object_or_404
from rest_framework.generics import ListAPIView


class Actorlist(ListAPIView):
    queryset = Actors.objects.all()
    serializer_class = ActorlistSerializers

class Screenwriterlist(ListAPIView):
    queryset = Screenwriter.objects.all()
    serializer_class = ScreenwriterlistSerializers

class Directorlist(ListAPIView):
    queryset = Director.objects.all()
    serializer_class = DirectorlistSerializers

class Newslist(ListAPIView):
    queryset = News.objects.all()
    serializer_class = NewslistSerializers
# --------------------------------------------------------------------------
@api_view(['GET'])
def Directordetail(request, director_id):
    director = get_object_or_404(Director, id=director_id)
    serializer = DirectordetaileSerializers(director)
    return Response(serializer.data)

@api_view(['GET'])
def Screenwriterdetail(request, screenwriter_id):
    screenwriter = get_object_or_404(Screenwriter, id=screenwriter_id)
    serializer = ScreenwriterdetaileSerializers(screenwriter)
    return Response(serializer.data)

@api_view(['GET'])
def Actordetail(request, actor_id):
    actor = get_object_or_404(Actors, id=actor_id)
    serializer = ActordetaileSerializers(actor)
    return Response(serializer.data)

@api_view(['GET'])
def Newsdetail(request, new_id):
    news = get_object_or_404(News, id=new_id)
    serializer = NewsdetailSerializers(news)
    return Response(serializer.data)

@api_view(['GET'])
def Studiohistory(requst):
    studiohistory = StudioHistory.objects.all() 
    serializer = StudiohistorySerializers(studiohistory, many=True)
    return Response(serializer.data)

@api_view(['GET'])
def StudiohistorySSSR(requst):
    studiohistorysssr = StudioHistorySSSR.objects.all() 
    serializer = StudiohistorySSSRSerializers(studiohistorysssr, many=True)
    return Response(serializer.data)