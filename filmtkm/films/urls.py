from django.urls import path
from . import views

urlpatterns = [
    path('film_list/',views.Filmlist.as_view()),
    path('film_details/<int:film_id>/',views.Filmsdetail),
    path('actor_list/',views.Actorlist.as_view()),
    path('actor_details/<int:actor_id>/',views.Actordetail),
    path('screenwriter_list/',views.Screenwriterlist.as_view()),
    path('screenwriter_details/<int:screenwriter_id>/',views.Screenwriterdetail),
    path('director_list/',views.Directorlist.as_view()),
    path('director_details/<int:director_id>/',views.Directordetail),
    path('new_list/',views.Newslist.as_view()),
    path('new_details/<int:new_id>/',views.Newsdetail),
    path('studiohistory/',views.Studiohistory),
    path('studiohistory/sssr',views.StudiohistorySSSR),
    path('trailer_list/', views.Trailorlist.as_view()),
    path('trailer_details/<int:trailor_id>/', views.Trailordetail),
    path('images/',views.Imagehis.as_view())
]