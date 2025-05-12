# from django.contrib import admin
# from django.utils.html import format_html
#
#
# @admin.register(Actors)
# class ActorAdmin(admin.ModelAdmin):
#     list_display = ['surat', 'name', 'surname', 'father_name']
#
#     def surat(request, obj: Actors):
#         try:
#             return format_html(f'<img src="{obj.image.url}"')
#         except:
#             return None
#
#
# @admin.register(Rez)
# class RezAdmin(admin.ModelAdmin):
#     list_display = ['surat', 'name', 'surname', 'father_name']
#
#     def surat(request, obj: Actors):
#         try:
#             return format_html(f'<img src="{obj.image.url}"')
#         except:
#             return None
#
#
# @admin.register(Film)
# class FilmAdmin(admin.ModelAdmin):
#     list_display = ['id','name', 'rez', 'description']

from django.contrib import admin
from .models import Company, Product

@admin.register(Company)
class CompanyAdmin(admin.ModelAdmin):
    list_display = ('name',)
    search_fields = ('name',)

@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
    list_display = ('name', 'price', 'get_companies')
    search_fields = ('name',)
    filter_horizontal = ('companies',)  # Удобный интерфейс для ManyToManyField

    def get_companies(self, obj):
        return ", ".join([company.name for company in obj.companies.all()])
    get_companies.short_description = 'Компании'