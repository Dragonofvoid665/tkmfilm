from rest_framework import viewsets
from .models import Actors, Film, Screenwriter, Director
from .serializers import ActorsSerializer, FilmSerializer, ScreenwriterSerializer, DirectorSerializer
from django.shortcuts import render, get_object_or_404

# API Views
class ActorsViewSet(viewsets.ModelViewSet):
    queryset = Actors.objects.all()
    serializer_class = ActorsSerializer

class FilmViewSet(viewsets.ModelViewSet):
    queryset = Film.objects.all()
    serializer_class = FilmSerializer

class ScreenwriterViewSet(viewsets.ModelViewSet):
    queryset = Screenwriter.objects.all()
    serializer_class = ScreenwriterSerializer

class DirectorViewSet(viewsets.ModelViewSet):
    queryset = Director.objects.all()
    serializer_class = DirectorSerializer

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
    actors = film.actors.all()  
    screenwriters = film.screenwriters.all()
    directors = film.director.all()
    return render(request, 'films/films_details.html', {'film': film, 'actors': actors,'screenwriters':screenwriters,'directors':directors})

def screenwriter_list(request):
    screenwriters = Screenwriter.objects.all()
    return render(request, 'films/screenwriter_list.html', {'screenwriters': screenwriters})

def screenwriter_detail(request, screenwriter_id):
    screenwriter = get_object_or_404(Screenwriter, id=screenwriter_id)
    films = screenwriter.Films.all() 
    return render(request, 'films/screenwriter_detail.html', {'screenwriter': screenwriter, 'films': films})

def director_list(request):
    directors = Director.objects.all()
    return render(request, 'films/director_list.html', {'directors': directors})

def director_detail(request, director_id):
    director = get_object_or_404(Director, id=director_id)
    films = director.Films.all() 
    return render(request, 'films/director_detail.html', {'director': director, 'films': films})