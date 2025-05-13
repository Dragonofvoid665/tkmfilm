from django.contrib import admin
from .models import Actors, Film
from django.utils.html import format_html

@admin.register(Actors)
class MainCategoryAdmin(admin.ModelAdmin):
    exclude = ['image_base64']
    list_display = ['id', 'name_rus','name_eng','name_tkm','surname_rus','surname_tkm','surname_eng','father_name_rus','father_name_tkm','father_name_eng', 'picture', "picture_size","year"]
    search_fields = ['name_rus','name_eng','name_tkm','surname_rus','surname_tkm','surname_eng','father_name_rus','father_name_tkm','father_name_eng','year']
    def picture(self, obj:Actors):
        return format_html(f'<img src="{obj.image_base64}" width="200px">')
    def picture_size(self, obj:Actors):
        try:
            return format_html(f'{len(obj.image_base64)}')
        except:
            return 0


@admin.register(Film)
class FilmAdmin(admin.ModelAdmin):
    list_display = ['id', 'name_rus','name_eng','name_tkm','description_rus','description_eng','description_tkm']
    search_fields = ['name_rus','name_eng','name_tkm','description_rus','description_eng','description_tkm']
    filter_horizontal = ('actors',)

    def get_companies(self, obj):
        return ", ".join([company.name for company in obj.companies.all()])
    get_companies.short_description = 'Компании'
