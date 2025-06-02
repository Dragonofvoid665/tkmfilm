from django.contrib import admin
from .models import *
from django.forms import TextInput
from django.utils.html import format_html

@admin.register(Actors)
class ActorAdmin(admin.ModelAdmin):
    exclude = ['image_base64']
    list_display = ['id', 'name_rus', 'name_eng', 'name_tkm', 'surname_rus', 'surname_tkm', 'surname_eng', 'father_name_rus', 'father_name_tkm', 'father_name_eng', 'picture','birth_date', 'sssr_or_not','place_of_birth_eng','place_of_birth_rus','place_of_birth_tkm','short_biography_rus','short_biography_tkm','short_biography_eng']
    search_fields = ['name_rus', 'name_eng', 'name_tkm', 'surname_rus', 'surname_tkm', 'surname_eng', 'father_name_rus', 'father_name_tkm', 'father_name_eng', 'birth_date']
    def picture(self, obj:Actors):
        return format_html(f'<img src="{obj.image}" width="200px">')
    def short_biography_rus(self, obj): 
        return obj.biography_rus[:20] + '...' if len(obj.biography_rus) > 10 else obj.biography_rus
    short_biography_rus.short_description = 'Биография на Русском'
    def short_biography_eng(self, obj): 
        return obj.biography_eng[:20] + '...' if len(obj.biography_eng) > 10 else obj.biography_eng
    short_biography_eng.short_description = 'Биография на Туркменском'
    def short_biography_tkm(self, obj): 
        return obj.biography_tkm[:20] + '...' if len(obj.biography_tkm) > 10 else obj.biography_tkm
    short_biography_tkm.short_description = 'Биография на Английском'
@admin.register(Screenwriter)
class ScreenwriterAdmin(admin.ModelAdmin):
    list_display = ['id', 'name_rus', 'name_eng', 'name_tkm', 'surname_rus', 'surname_eng', 'surname_tkm', 'father_name_rus', 'father_name_eng', 'father_name_tkm', 'short_biography_rus', 'short_biography_eng', 'short_biography_tkm', 'birth_date', 'picture','sssr_or_not','place_of_birth_eng','place_of_birth_rus','place_of_birth_tkm']
    search_fields = ['name_rus', 'name_eng', 'name_tkm', 'surname_rus', 'surname_tkm', 'surname_eng', 'father_name_rus', 'father_name_tkm', 'father_name_eng', 'birth_date']
    def picture(self, obj:Screenwriter):
        return format_html(f'<img src="{obj.image}" width="200px">')
    def short_biography_rus(self, obj): 
        return obj.biography_rus[:20] + '...' if len(obj.biography_rus) > 10 else obj.biography_rus
    short_biography_rus.short_description = 'Биография на Русском'
    def short_biography_eng(self, obj): 
        return obj.biography_eng[:20] + '...' if len(obj.biography_eng) > 10 else obj.biography_eng
    short_biography_eng.short_description = 'Биография на Туркменском'
    def short_biography_tkm(self, obj): 
        return obj.biography_tkm[:20] + '...' if len(obj.biography_tkm) > 10 else obj.biography_tkm
    short_biography_tkm.short_description = 'Биография на Английском'
@admin.register(Film)
class FilmAdmin(admin.ModelAdmin):
    list_display = ['id', 'name_rus', 'name_en', 'name_tk', 'short_description_ru', 'short_description_en', 'short_description_tk', 'picture', 'year', 'sssr_or_not','kadr1','kadr2','kadr3','kadr4']
    search_fields = ['name_rus', 'name_en', 'name_tk', 'description_ru', 'description_en', 'description_tk', 'genre_en', 'genre_tk', 'genre_ru', 'sssr_or_not']
    filter_horizontal = ('actors','screenwriter','director')  # Только actors остаётся в filter_horizontal
    list_filter = ['sssr_or_not', 'year']
    def short_description_en(self, obj): 
        return obj.description_en[:20] + '...' if len(obj.description_en) > 10 else obj.description_en 
    short_description_en.short_description = 'Описание (EN)' 
 
    def short_description_tk(self, obj): 
        return obj.description_tk[:20] + '...' if len(obj.description_tk) > 10 else obj.description_tk 
    short_description_tk.short_description = 'Описание (TM)' 
 
    def short_description_ru(self, obj): 
        return obj.description_ru[:20] + '...' if len(obj.description_ru) > 10 else obj.description_ru 
    short_description_ru.short_description = 'Описание (RU)'
    def picture(self, obj: Film):
        return format_html(f'<img src="{obj.image}" width="200px">')

    def save_model(self, request, obj, form, change):
        super().save_model(request, obj, form, change)

    def save_related(self, request, form, formsets, change):
        super().save_related(request, form, formsets, change)


@admin.register(Director)
class DirectorAdmin(admin.ModelAdmin):
    list_display = ['id', 'name_rus', 'name_eng', 'name_tkm', 'surname_rus', 'surname_eng', 'surname_tkm', 'father_name_rus', 'father_name_eng', 'father_name_tkm', 'short_biography_rus', 'short_biography_eng', 'short_biography_tkm', 'birth_date','picture', 'sssr_or_not','place_of_birth_eng','place_of_birth_rus','place_of_birth_tkm']
    search_fields = ['name_rus', 'name_eng', 'name_tkm', 'surname_rus', 'surname_eng', 'surname_tkm', 'father_name_rus', 'father_name_eng', 'father_name_tkm', 'short_biography_rus', 'short_biography_eng', 'short_biography_tkm', 'birth_date','picture', 'sssr_or_not','place_of_birth_eng','place_of_birth_rus','place_of_birth_tkm']    
    def picture(self, obj:Director):
        return format_html(f'<img src="{obj.image}" width="200px">')
    def short_biography_rus(self, obj): 
        return obj.biography_rus[:20] + '...' if len(obj.biography_rus) > 10 else obj.biography_rus
    short_biography_rus.short_description = 'Биография на Русском'
    def short_biography_eng(self, obj): 
        return obj.biography_eng[:20] + '...' if len(obj.biography_eng) > 10 else obj.biography_eng
    short_biography_eng.short_description = 'Биография на Туркменском'
    def short_biography_tkm(self, obj): 
        return obj.biography_tkm[:20] + '...' if len(obj.biography_tkm) > 10 else obj.biography_tkm
    short_biography_tkm.short_description = 'Биография на Английском'
    
@admin.register(News)
class NewsAdmin(admin.ModelAdmin):

    list_display = ['id', 'picture','title_rus', 'title_eng', 'title_tkm', 'content_rus', 'content_eng', 'content_tkm', 'publication_date']
    def picture(self, obj:News):
        return format_html(f'<img src="{obj.image}" width="200px">')

        
@admin.register(StudioHistory)
class StudioHistoryAdmin(admin.ModelAdmin):
    list_display = ['id','short_text_rus', 'short_text_eng', 'short_text_tkm', 'short_creator_bio_rus', 'short_creator_bio_eng', 'short_creator_bio_tkm', 'found_date', 'creator_birth_date']
    filter_horizontal = ('imagehistory',)
    def short_text_rus(self, obj): 
        return obj.text_rus[:20] + '...' if len(obj.text_rus) > 10 else obj.text_rus
    short_text_rus.short_description = 'Информация о студии на Русском'
    def short_text_eng(self, obj): 
        return obj.text_eng[:20] + '...' if len(obj.text_eng) > 10 else obj.text_eng
    short_text_eng.short_description = 'Информация о студии на Русском'
    def short_text_tkm(self, obj): 
        return obj.text_tkm[:20] + '...' if len(obj.text_rus) > 10 else obj.text_tkm
    short_text_tkm.short_description = 'Информация о студии на Русском'
#-----------------------------------------------------------------------------------------------------------------------------------------
    def short_creator_bio_rus(self, obj): 
        return obj. creator_bio_rus[:20] + '...' if len(obj. creator_bio_rus) > 10 else obj. creator_bio_rus
    short_creator_bio_rus.short_description = 'Биография создателя на Русском'
    def short_creator_bio_eng(self, obj): 
        return obj.creator_bio_eng[:20] + '...' if len(obj.creator_bio_eng) > 10 else obj.creator_bio_eng
    short_creator_bio_eng.short_description = 'Биография создателя на Туркменском'
    def short_creator_bio_tkm(self, obj): 
        return obj.creator_bio_tkm[:20] + '...' if len(obj.creator_bio_tkm) > 10 else obj.creator_bio_tkm
    short_creator_bio_tkm.short_description = 'Биография создателя на Английском'


@admin.register(StudioHistorySSSR)
class StudioHistoryAdmin(admin.ModelAdmin):
    list_display = ['id','short_text_rus', 'short_text_eng', 'short_text_tkm','found_date']
    filter_horizontal = ('imagehistorysssr',)
    def short_text_rus(self, obj): 
        return obj.text_rus[:20] + '...' if len(obj.text_rus) > 10 else obj.text_rus
    short_text_rus.short_description = 'Информация о студии на Русском'
    def short_text_eng(self, obj): 
        return obj.text_eng[:20] + '...' if len(obj.text_eng) > 10 else obj.text_eng
    short_text_eng.short_description = 'Информация о студии на Русском'
    def short_text_tkm(self, obj): 
        return obj.text_tkm[:20] + '...' if len(obj.text_rus) > 10 else obj.text_tkm
    short_text_tkm.short_description = 'Информация о студии на Русском'
    
@admin.register(Imagehistory)
class ImagehistoryAdmin(admin.ModelAdmin):
    list_display=['id','image']
    

@admin.register(ImagehistorySSSR)
class ImagehistorySSSRAdmin(admin.ModelAdmin):
    list_display=['id','image']


@admin.register(Trailer)
class TrilerAdmin(admin.ModelAdmin):
    list_display = ['id','video']