from django.urls import path, include
from rest_framework.routers import DefaultRouter
from . import views

# API Router
router = DefaultRouter()
router.register(r'actors', views.ActorsViewSet)
router.register(r'films', views.FilmViewSet)
router.register(r'screenwriters', views.ScreenwriterViewSet)
router.register(r'directors', views.DirectorViewSet)

urlpatterns = [
    # API URLs
    path('api/', include(router.urls)),  # Маршруты для API
    # HTML URLs
    path('actors/', views.actors_list, name='actors_list'),
    path('actors/<int:actor_id>/', views.actor_detail, name='actor_detail'),
    path('films/', views.films_list, name='films_list'),
    path('films/<int:film_id>/', views.film_detail, name='film_detail'),
    path('screenwriters/', views.screenwriter_list, name='screenwriter_list'),
    path('screenwriters/<int:screenwriter_id>/', views.screenwriter_detail, name='screenwriter_detail'),
    path('directors/', views.director_list, name='director_list'),
    path('directors/<int:director_id>/', views.director_detail, name='director_detail'),
]