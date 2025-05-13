from django.contrib import admin
from .models import Actors, Film, Screenwriter, Director, News, StudioHistory
from django.utils.html import format_html

@admin.register(Actors)
class ActorAdmin(admin.ModelAdmin):
    exclude = ['image_base64']
    list_display = ['id', 'name_rus', 'name_eng', 'name_tkm', 'surname_rus', 'surname_tkm', 'surname_eng', 'father_name_rus', 'father_name_tkm', 'father_name_eng', 'picture', 'picture_size', 'birth_date']
    search_fields = ['name_rus', 'name_eng', 'name_tkm', 'surname_rus', 'surname_tkm', 'surname_eng', 'father_name_rus', 'father_name_tkm', 'father_name_eng', 'birth_date']
    # filter_horizontal = ('films',)  # Для обратного отношения

    def picture(self, obj: Actors):
        return format_html(f'<img src="{obj.image_base64}" width="200px">')

    def picture_size(self, obj: Actors):
        try:
            return format_html(f'{len(obj.image_base64)}')
        except:
            return 0

@admin.register(Screenwriter)
class ScreenwriterAdmin(admin.ModelAdmin):
    exclude = ['image_base64']
    list_display = ['id', 'name_rus', 'name_eng', 'name_tkm', 'surname_rus', 'surname_eng', 'surname_tkm', 'father_name_rus', 'father_name_eng', 'father_name_tkm', 'biography_rus', 'biography_eng', 'biography_tkm', 'birth_date', 'picture', 'picture_size']
    search_fields = ['name_rus', 'name_eng', 'name_tkm', 'surname_rus', 'surname_tkm', 'surname_eng', 'father_name_rus', 'father_name_tkm', 'father_name_eng', 'birth_date']

    def picture(self, obj: Screenwriter):
        return format_html(f'<img src="{obj.image_base64}" width="200px">')

    def picture_size(self, obj: Screenwriter):
        try:
            return format_html(f'{len(obj.image_base64)}')
        except:
            return 0
        

@admin.register(Film)
class FilmAdmin(admin.ModelAdmin):
    list_display = ['id', 'name_rus', 'name_eng', 'name_tkm', 'description_rus', 'description_eng', 'description_tkm', 'picture', 'picture_size']
    search_fields = ['name_rus', 'name_eng', 'name_tkm', 'description_rus', 'description_eng', 'description_tkm']
    filter_horizontal = ('actors','screenwriters','director',)
    exclude = ['image_base64']

    def picture(self, obj: Film):
        return format_html(f'<img src="{obj.image_base64}" width="200px">')

    def picture_size(self, obj: Film):
        try:
            return format_html(f'{len(obj.image_base64)}')
        except:
            return 0

    def save_model(self, request, obj, form, change):
        # Сохраняем объект Film без связей многие-ко-многим
        super().save_model(request, obj, form, change)
    def save_related(self, request, form, formsets, change):
        # Сохраняем связи многие-ко-многим после сохранения объекта
        super().save_related(request, form, formsets, change)


@admin.register(Director)
class DirectorAdmin(admin.ModelAdmin):
    exclude = ['image_base64']
    list_display = ['id', 'name_rus', 'name_eng', 'name_tkm', 'surname_rus', 'surname_eng', 'surname_tkm', 'father_name_rus', 'father_name_eng', 'father_name_tkm', 'biography_rus', 'biography_eng', 'biography_tkm', 'birth_date','picture', 'picture_size',]
    search_fields = ['name_rus', 'name_eng', 'name_tkm', 'surname_rus', 'surname_tkm', 'surname_eng', 'father_name_rus', 'father_name_tkm', 'father_name_eng', 'birth_date']    

    def picture(self, obj: Director):
        return format_html(f'<img src="{obj.image_base64}" width="200px">')


    def picture_size(self, obj: Director):
        try:
            return format_html(f'{len(obj.image_base64)}')
        except:
            return 
        
@admin.register(News)
class NewsAdmin(admin.ModelAdmin):
    exclude = ['image_base64']
    list_display = ['id', 'picture', 'picture_size', 'title_rus', 'title_eng', 'title_tkm', 'content_rus', 'content_eng', 'content_tkm', 'publication_date']
    
    def picture(self, obj: News):
        return format_html(f'<img src="{obj.image_base64}" width="200px">')


    def picture_size(self, obj: News):
        try:
            return format_html(f'{len(obj.image_base64)}')
        except:
            return 
        
@admin.register(StudioHistory)
class StudioHistoryAdmin(admin.ModelAdmin):
    exclude = ['image_base64']
    list_display = ['id', 'picture', 'picture_size', 'text_rus', 'text_eng', 'text_tkm', 'creator_bio_rus', 'creator_bio_eng', 'creator_bio_tkm', 'found_date', 'creator_birth_date']
     
    def picture(self, obj: StudioHistory):
        return format_html(f'<img src="{obj.image_base64}" width="200px">')


    def picture_size(self, obj: StudioHistory):
        try:
            return format_html(f'{len(obj.image_base64)}')
        except:
            return