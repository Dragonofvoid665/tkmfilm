from django.db import models
from PIL import Image
from io import BytesIO
import base64
from django.core.validators import FileExtensionValidator

class PersonModel(models.Model):
    image = models.ImageField(
        null=False,
        blank=False,
        upload_to="static/images/",

        verbose_name="Фотография",
        help_text="Нельзя оставить пустым!",
    )
    name_rus = models.CharField(
        max_length=100,
        null=False,
        blank=False,
        verbose_name="Имя на русском",
        help_text="Нельзя оставить пустым"
    )
    name_eng = models.CharField(
        max_length=100,
        null=False,
        blank=False,
        verbose_name="Имя на английском",
        help_text="Нельзя оставить пустым"
    )
    name_tkm = models.CharField(
        max_length=100,
        null=False,
        blank=False,
        verbose_name="Имя на туркменском",
        help_text="Нельзя оставить пустым"
    )
    surname_rus = models.CharField(
        max_length=100,
        null=False,
        blank=False,
        verbose_name="Фамилия на русском",
        help_text="Нельзя оставить пустым"
    )
    surname_eng = models.CharField(
        max_length=100,
        null=False,
        blank=False,
        verbose_name="Фамилия на английском",
        help_text="Нельзя оставить пустым"
    )
    surname_tkm = models.CharField(
        max_length=100,
        null=False,
        blank=False,
        verbose_name="Фамилия на туркменском",
        help_text="Нельзя оставить пустым"
    )
    father_name_rus = models.CharField(
        max_length=50,
        null=False,
        blank=False,
        verbose_name="Отчество на русском",
        help_text="Нельзя оставить пустым"
    )
    father_name_eng = models.CharField(
        max_length=50,
        null=False,
        blank=False,
        verbose_name="Отчество на английском",
        help_text="Нельзя оставить пустым"
    )
    father_name_tkm = models.CharField(
        max_length=50,
        null=False,
        blank=False,
        verbose_name="Отчество на туркменском",
        help_text="Нельзя оставить пустым"
    )
    biography_rus = models.TextField(
        null=False,
        blank=False,
        verbose_name="Биография на русском",
        help_text="Нельзя оставить пустым"
    )
    biography_eng = models.TextField(
        null=False,
        blank=False,
        verbose_name="Биография на английском",
        help_text="Нельзя оставить пустым"
    )
    biography_tkm = models.TextField(
        null=False,
        blank=False,
        verbose_name="Биография на туркменском",
        help_text="Нельзя оставить пустым"
    )
    birth_date = models.DateField(
        null=False,
        blank=False,
        verbose_name="Дата рождения",
        help_text="Нельзя оставить пустым"
    )
    sssr_or_not = models.BooleanField(default=False)
    place_of_birth_eng = models.CharField(max_length=100, null=False, blank=False, default='Turkmenistan')
    place_of_birth_rus = models.CharField(max_length=100, null=False, blank=False, default='Turkmenistan')
    place_of_birth_tkm = models.CharField(max_length=100, null=False, blank=False, default='Turkmenistan')
    
    def __str__(self):
        return f"{self.name_rus} {self.surname_rus}"

    class Meta:
        abstract = True

class Actors(PersonModel):
    class Meta:
        verbose_name = "Актёр"
        verbose_name_plural = "Актёры"

class Screenwriter(PersonModel):
    class Meta:
        verbose_name = "Сценарист"
        verbose_name_plural = "Сценаристы"
    

class Director(PersonModel):
    class Meta:
        verbose_name = "Режиссёр"
        verbose_name_plural = "Режиссёры"


class Film(models.Model):
    image = models.ImageField(
        null=False,
        blank=False,
        upload_to="static/images/",
        verbose_name="Фотография",
        help_text="Нельзя оставить пустым!",
    )
    name_rus = models.CharField(
        max_length=200,
        null=False,
        blank=False,
        verbose_name="Название фильма на русском",
        help_text="Нельзя оставить пустым"
    )
    name_en = models.CharField(
        max_length=200,
        null=False,
        blank=False,
        verbose_name="Название фильма на английском",
        help_text="Нельзя оставить пустым"
    )
    name_tk = models.CharField(
        max_length=200,
        null=False,
        blank=False,
        verbose_name="Название фильма на туркменском",
        help_text="Нельзя оставить пустым"
    )
    description_ru = models.TextField(
        null=False,
        blank=False,
        verbose_name="Описание фильма на русском",
        help_text="Нельзя оставить пустым"
    )
    description_en = models.TextField(
        null=False,
        blank=False,
        verbose_name="Описание фильма на английском",
        help_text="Нельзя оставить пустым"
    )
    description_tk = models.TextField(
        null=False,
        blank=False,
        verbose_name="Описание фильма на туркменском",
        help_text="Нельзя оставить пустым"
    )
    genre_en = models.CharField(
        max_length=100,
        null=False,
        blank=False,
        verbose_name="Жанр фильма на английском",
        help_text="Нельзя оставить пустым"
    )
    genre_ru = models.CharField(
        max_length=100,
        null=False,
        blank=False,
        verbose_name="Жанр фильма на русском",
        help_text="Нельзя оставить пустым"
    )
    genre_tk = models.CharField(
        max_length=100,
        null=False,
        blank=False,
        verbose_name="Жанр фильма на туркменском",
        help_text="Нельзя оставить пустым"
    )
    sssr_or_not = models.BooleanField(
        default=False,
        verbose_name="Снят при СССР или нет",
        help_text="Нельзя оставлять пустым"
    )
    actors = models.ManyToManyField(Actors, related_name="films")
    screenwriter = models.ManyToManyField(Screenwriter, related_name="films")
    director = models.ManyToManyField(Director, related_name="films")
    year = models.IntegerField(
        default=2020,
        blank=False,
        null=False)
    kadr1 = models.ImageField(
        default="static/images/25.jpg",
        upload_to = "static/kadr/",
        null=False,
        blank=False,
        verbose_name="Фотография",
        help_text="Нельзя оставить пустым!",
    )
    kadr2 = models.ImageField(
        default="static/images/25.jpg",
        upload_to = "static/kadr/",
        null=False,
        blank=False,
        verbose_name="Фотография",
        help_text="Нельзя оставить пустым!",
    )
    kadr3 = models.ImageField(
        default="static/images/25.jpg",
        upload_to = "static/kadr/",
        null=False,
        blank=False,
        verbose_name="Фотография",
        help_text="Нельзя оставить пустым!",
    )
    kadr4 = models.ImageField(
        upload_to = "static/kadr/",
        default="static/images/25.jpg",
        null=False,
        blank=False,
        verbose_name="Фотография",
        help_text="Нельзя оставить пустым!",
    )
    
    def __str__(self):
        return self.name_rus

    class Meta:
        verbose_name = "Фильм"
        verbose_name_plural = "Фильмы"

    
class News(models.Model):
    image = models.ImageField(
        null=False,
        blank=False,
        upload_to="static/images/",
        verbose_name="Фотография",
        help_text="Нельзя оставить пустым!",
    )
    title_rus = models.CharField(
        max_length=200,
        null=False,
        blank=False,
        verbose_name="Заголовок новости на русском",
        help_text="Нельзя оставить пустым"
    )
    title_eng = models.CharField(
        max_length=200,
        null=False,
        blank=False,
        verbose_name="Заголовок новости на английском",
        help_text="Нельзя оставить пустым"
    )
    title_tkm = models.CharField(
        max_length=200,
        null=False,
        blank=False,
        verbose_name="Заголовок новости на туркменском",
        help_text="Нельзя оставить пустым"
    )
    short_content_rus = models.TextField(
        null=False,
        blank=False,
        verbose_name="Краткое описание новостей на русском",
        help_text="Нельзя оставить пустым"
    )
    short_content_eng = models.TextField(
        null=False,
        blank=False,
        verbose_name="Краткое описание новостей на английском",
        help_text="Нельзя оставить пустым"
    )
    short_content_tkm = models.TextField(
        null=False,
        blank=False,
        verbose_name="Краткое описание новостейна туркменском",
        help_text="Нельзя оставить пустым"
    )
    content_rus = models.TextField(
        null=False,
        blank=False,
        verbose_name="описание новостей на русском",
        help_text="Нельзя оставить пустым"
    )
    content_eng = models.TextField(
        null=False,
        blank=False,
        verbose_name="описание новостей на английском",
        help_text="Нельзя оставить пустым"
    )
    content_tkm = models.TextField(
        null=False,
        blank=False,
        verbose_name="описание новостей на туркменском",
        help_text="Нельзя оставить пустым"
    )
    publication_date = models.DateField(
        null=False,
        blank=False,
        verbose_name="Дата публикации",
        help_text="Нельзя оставить пустым"
    )

    def __str__(self):
        return self.title_rus

    class Meta:
        verbose_name = "Новость"
        verbose_name_plural = "Новости"

class Imagehistory(models.Model):
    image = models.ImageField(
        upload_to='static/images',
        null=False,
        blank=False,
        verbose_name="Фотография",
        help_text="Нельзя оставить пустым!",
    )

class ImagehistorySSSR(models.Model):
    image = models.ImageField(
        upload_to='static/images',
        null=False,
        blank=False,
        verbose_name="Фотография",
        help_text="Нельзя оставить пустым!",
    )

class StudioHistory(models.Model):
    image = models.ImageField(
        null=False,
        blank=False,
        upload_to="static/images/",
        verbose_name="Фотография",
        help_text="Нельзя оставить пустым!",
    )
    text_rus = models.TextField(
        null=False,
        blank=False,
        verbose_name="Информация о студии на русском",
        help_text="Нельзя оставить пустым"
    )
    text_eng = models.TextField(
        null=False,
        blank=False,
        verbose_name="Информация о студии на английском",
        help_text="Нельзя оставить пустым"
    )
    text_tkm = models.TextField(
        null=False,
        blank=False,
        verbose_name="Информация о студии на туркменском",
        help_text="Нельзя оставить пустым"
    )
    creator_bio_rus = models.TextField(
        null=False,
        blank=False,
        verbose_name="Биография создателя студии на русском",
        help_text="Нельзя оставить пустым"
    )
    creator_bio_eng = models.TextField(
        null=False,
        blank=False,
        verbose_name="Биография создателя студии на английском",
        help_text="Нельзя оставить пустым"
    )
    creator_bio_tkm = models.TextField(
        null=False,
        blank=False,
        verbose_name="Биография создателя студии на туркменском",
        help_text="Нельзя оставить пустым"
    )
    found_date = models.DateField(
        null=False,
        blank=False,
        verbose_name="Дата основания студии",
        help_text="Нельзя оставить пустым"
    )
    creator_birth_date = models.DateField(
        null=False,
        blank=False,
        verbose_name="Дата рождения создателя",
        help_text="Нельзя оставить пустым"
    )

    def __str__(self):
        return "История студии"

    class Meta:
        verbose_name = "История студии"
        verbose_name_plural = "История студии"
    imagehistory = models.ManyToManyField(Imagehistory, related_name="history")

class StudioHistorySSSR(models.Model):
    text_rus = models.TextField(
        null=False,
        blank=False,
        verbose_name="Информация о студии на русском",
        help_text="Нельзя оставить пустым"
    )
    text_eng = models.TextField(
        null=False,
        blank=False,
        verbose_name="Информация о студии на английском",
        help_text="Нельзя оставить пустым"
    )
    text_tkm = models.TextField(
        null=False,
        blank=False,
        verbose_name="Информация о студии на туркменском",
        help_text="Нельзя оставить пустым"
    )
    found_date = models.DateField(
        null=False,
        blank=False,
        verbose_name="Дата основания студии",
        help_text="Нельзя оставить пустым"
    )
    def __str__(self):
        return "История студии в времена СССР"

    class Meta:
        verbose_name = "История студии в времена СССР"
        verbose_name_plural = "История студии в времена СССР"
    imagehistorysssr = models.ManyToManyField(ImagehistorySSSR, related_name="historysssr")

class Trailer(models.Model):
    video = models.FileField(
        upload_to="static/video/",
        verbose_name='Поставтье сюда трилер',
        help_text='Сюдв можно зашружать только видео'
    )
    class Meta:
        verbose_name = "Трилер"
        verbose_name_plural = "Трилеры"




