from django.contrib import admin
from .models import *
from django.utils.html import format_html

@admin.register(Actors)
class ActorAdmin(admin.ModelAdmin):
    list_display = ['id', 'name_rus', 'name_eng', 'name_tkm', 'surname_rus', 'surname_tkm', 'surname_eng', 'father_name_rus', 'father_name_tkm', 'father_name_eng', 'image','birth_date', 'sssr_or_not']
    search_fields = ['name_rus', 'name_eng', 'name_tkm', 'surname_rus', 'surname_tkm', 'surname_eng', 'father_name_rus', 'father_name_tkm', 'father_name_eng', 'birth_date']



@admin.register(Screenwriter)
class ScreenwriterAdmin(admin.ModelAdmin):
    list_display = ['id', 'name_rus', 'name_eng', 'name_tkm', 'surname_rus', 'surname_eng', 'surname_tkm', 'father_name_rus', 'father_name_eng', 'father_name_tkm', 'biography_rus', 'biography_eng', 'biography_tkm', 'birth_date', 'image','sssr_or_not']
    search_fields = ['name_rus', 'name_eng', 'name_tkm', 'surname_rus', 'surname_tkm', 'surname_eng', 'father_name_rus', 'father_name_tkm', 'father_name_eng', 'birth_date']



@admin.register(Film)
class FilmAdmin(admin.ModelAdmin):
    list_display = ['id', 'name_rus', 'name_eng', 'name_tkm', 'description_rus', 'description_eng', 'description_tkm', 'image']
    search_fields = ['name_rus', 'name_eng', 'name_tkm', 'description_rus', 'description_eng', 'description_tkm','genre_eng','genre_tkm','genre_rus','sssr_or_not']
    filter_horizontal = ('actors','screenwriters','director',)


    def save_model(self, request, obj, form, change):
        # Сохраняем объект Film без связей многие-ко-многим
        super().save_model(request, obj, form, change)
    def save_related(self, request, form, formsets, change):
        # Сохраняем связи многие-ко-многим после сохранения объекта
        super().save_related(request, form, formsets, change)


@admin.register(Director)
class DirectorAdmin(admin.ModelAdmin):
    list_display = ['id', 'name_rus', 'name_eng', 'name_tkm', 'surname_rus', 'surname_eng', 'surname_tkm', 'father_name_rus', 'father_name_eng', 'father_name_tkm', 'biography_rus', 'biography_eng', 'biography_tkm', 'birth_date','image', 'sssr_or_not']
    search_fields = ['name_rus', 'name_eng', 'name_tkm', 'surname_rus', 'surname_tkm', 'surname_eng', 'father_name_rus', 'father_name_tkm', 'father_name_eng', 'birth_date']    

    
@admin.register(News)
class NewsAdmin(admin.ModelAdmin):
    list_display = ['id', 'image','title_rus', 'title_eng', 'title_tkm', 'content_rus', 'content_eng', 'content_tkm', 'publication_date']


        
@admin.register(StudioHistory)
class StudioHistoryAdmin(admin.ModelAdmin):
    list_display = ['id', 'image','text_rus', 'text_eng', 'text_tkm', 'creator_bio_rus', 'creator_bio_eng', 'creator_bio_tkm', 'found_date', 'creator_birth_date']
     

@admin.register(StudioHistorySSSR)
class StudioHistoryAdmin(admin.ModelAdmin):
    list_display = ['id', 'image','text_rus', 'text_eng', 'text_tkm','found_date']
