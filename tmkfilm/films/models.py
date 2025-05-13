from django.db import models
from PIL import Image
from io import BytesIO
import base64

class MultilingualModel(models.Model):
    image = models.ImageField(
        null=False,
        blank=False,
        upload_to="static/images/",
        verbose_name="Фотография",
        help_text="Ставьте небольшие по объёму картинки. Нельзя оставить пустым!",
    )
    image_base64 = models.TextField(
        blank=True,
        null=True,
        verbose_name="Не трогать это поле!",
        help_text="Не трогать это поле!"
    )
    def save(self, *args, **kwargs):
        if self.image:
            img = Image.open(self.image)
            buffer = BytesIO()
            img_format = img.format.lower()
            img.save(buffer, format=img_format)

            image_base64_str = base64.b64encode(buffer.getvalue()).decode('utf-8')

            self.image_base64 = f"data:image/{img_format};base64,{image_base64_str}"


        super().save(*args, **kwargs)
    class Meta:
        abstract = True

# Абстрактный класс для персоналий
class PersonModel(MultilingualModel):
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


class Film(MultilingualModel):
    name_rus = models.CharField(
        max_length=200,
        null=False,
        blank=False,
        verbose_name="Название фильма на русском",
        help_text="Нельзя оставить пустым"
    )
    name_eng = models.CharField(
        max_length=200,
        null=False,
        blank=False,
        verbose_name="Название фильма на английском",
        help_text="Нельзя оставить пустым"
    )
    name_tkm = models.CharField(
        max_length=200,
        null=False,
        blank=False,
        verbose_name="Название фильма на туркменском",
        help_text="Нельзя оставить пустым"
    )
    description_rus = models.TextField(
        null=False,
        blank=False,
        verbose_name="Описание фильма на русском",
        help_text="Нельзя оставить пустым"
    )
    description_eng = models.TextField(
        null=False,
        blank=False,
        verbose_name="Описание фильма на английском",
        help_text="Нельзя оставить пустым"
    )
    description_tkm = models.TextField(
        null=False,
        blank=False,
        verbose_name="Описание фильма на туркменском",
        help_text="Нельзя оставить пустым"
    )
    actors = models.ManyToManyField(Actors, related_name="Films")
    screenwriters = models.ManyToManyField(Screenwriter, related_name="Films")
    director = models.ManyToManyField(Director,related_name="Films")

    def __str__(self):
        return self.name_rus

    class Meta:
        verbose_name = "Фильм"
        verbose_name_plural = "Фильмы"

class News(MultilingualModel):
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
    content_rus = models.TextField(
        null=False,
        blank=False,
        verbose_name="Текст новости на русском",
        help_text="Нельзя оставить пустым"
    )
    content_eng = models.TextField(
        null=False,
        blank=False,
        verbose_name="Текст новости на английском",
        help_text="Нельзя оставить пустым"
    )
    content_tkm = models.TextField(
        null=False,
        blank=False,
        verbose_name="Текст новости на туркменском",
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

class StudioHistory(MultilingualModel):
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