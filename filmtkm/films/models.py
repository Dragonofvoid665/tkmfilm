from django.db import models

class PersonModel(models.Model):
    image = models.ImageField(
        null=False,
        blank=False,
        upload_to="media/images/",

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
        upload_to="media/images/",

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
    genre_eng = models.CharField(
        max_length=100,
        null=False,
        blank=False,
        verbose_name="Жанр фильма на анлийском",
        help_text="Нельзя оставить пустым"
    )
    genre_rus = models.CharField(
        max_length=100,
        null=False,
        blank=False,
        verbose_name="Жанр фильма на русском",
        help_text="Нельзя оставить пустым"
    )
    genre_tkm = models.CharField(
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
    screenwriters = models.ManyToManyField(Screenwriter, related_name="films")
    director = models.ManyToManyField(Director, related_name="films")

    def __str__(self):
        return self.name_rus

    class Meta:
        verbose_name = "Фильм"
        verbose_name_plural = "Фильмы"

class News(models.Model):
    image = models.ImageField(
        null=False,
        blank=False,
        upload_to="media/images/",

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

class StudioHistory(models.Model):
    image = models.ImageField(
        null=False,
        blank=False,
        upload_to="media/images/",
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

class StudioHistorySSSR(models.Model):
    image = models.ImageField(
        null=False,
        blank=False,
        upload_to="media/images/",
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