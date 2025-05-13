from django.contrib import admin
from .models import Actors, Film
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

@admin.register(Film)
class FilmAdmin(admin.ModelAdmin):
    list_display = ['id', 'name_rus', 'name_eng', 'name_tkm', 'description_rus', 'description_eng', 'description_tkm', 'picture', 'picture_size']
    search_fields = ['name_rus', 'name_eng', 'name_tkm', 'description_rus', 'description_eng', 'description_tkm']
    filter_horizontal = ('actors',)
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