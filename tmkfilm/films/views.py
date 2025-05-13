from rest_framework import viewsets
from .models import Actors, Film
from .serializers import ActorsSerializer, FilmSerializer
from django.shortcuts import render, get_object_or_404

# API Views
class ActorsViewSet(viewsets.ModelViewSet):
    queryset = Actors.objects.all()
    serializer_class = ActorsSerializer

class FilmViewSet(viewsets.ModelViewSet):
    queryset = Film.objects.all()
    serializer_class = FilmSerializer

# HTML Views
def actors_list(request):
    actors = Actors.objects.all()
    return render(request, 'films/actors_list.html', {'actors': actors})

def actor_detail(request, actor_id):
    actor = get_object_or_404(Actors, id=actor_id)
    films = actor.Films.all() 
    return render(request, 'films/actors_detail.html', {'actor': actor, 'films': films})

def films_list(request):
    films = Film.objects.all()
    return render(request, 'films/films_list.html', {'films': films})

def film_detail(request, film_id):
    film = get_object_or_404(Film, id=film_id)
    actors = film.actors.all()  # Получаем связанных актёров
    return render(request, 'films/films_details.html', {'film': film, 'actors': actors})