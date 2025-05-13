from django.db import models
from PIL import Image
from io import BytesIO
import base64
from django.core.validators import FileExtensionValidator
from django.core.exceptions import ValidationError

class Actors(models.Model):
    image = models.ImageField(
        null=False,
        blank=False,
        upload_to="static/images/",
        verbose_name='Фотография актёра',
        help_text="Ставьте небольшого объема картинки. Нельзя оставить пустым!",
    )
    image_base64 = models.TextField(
        blank=True,
        null=True,
        verbose_name='Не трогать это поле!',
        help_text="Не трогать это поле!"
    )
    name_rus = models.CharField(
        max_length=50,
        null=False,
        blank=False,
        unique=False,
        verbose_name="Имя актёра на русском",
        help_text="Нельзя оставить пустым"
    )
    name_eng = models.CharField(
        max_length=50,
        null=False,
        blank=False,
        unique=False,
        verbose_name="Имя актёра на английском",
        help_text="Нельзя оставить пустым"
    )
    name_tkm = models.CharField(
        max_length=50,
        null=False,
        blank=False,
        unique=False,
        verbose_name="Имя актёра на туркменском",
        help_text="Нельзя оставить пустым",
        default="Atsyz"
    )
    surname_rus = models.CharField(
        max_length=50,
        null=False,
        blank=False,
        unique=False,
        verbose_name="Фамилия актёра на русском",
        help_text="Нельзя оставить пустым"
    )
    surname_eng = models.CharField(
        max_length=50,
        null=False,
        blank=False,
        unique=False,
        verbose_name="Фамилия актёра на английском",
        help_text="Нельзя оставить пустым"
    )
    surname_tkm = models.CharField(
        max_length=50,
        null=False,
        blank=False,
        unique=False,
        verbose_name="Фамилия актёра на туркменском",
        help_text="Нельзя оставить пустым",
        default="Atsyz"
    )
    father_name_rus = models.CharField(
        max_length=50,
        null=False,
        blank=False,
        unique=False,
        verbose_name="Отчество актёра на русском",
        help_text="Нельзя оставить пустым"
    )
    father_name_eng = models.CharField(
        max_length=50,
        null=False,
        blank=False,
        unique=False,
        verbose_name="Отчество актёра на английском",
        help_text="Нельзя оставить пустым"
    )
    father_name_tkm = models.CharField(
        max_length=50,
        null=False,
        blank=False,
        unique=False,
        verbose_name="Отчество актёра на туркменском",
        help_text="Нельзя оставить пустым",
        default="Atsyz"
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
    year = models.DateField(
        null=False,
        blank=False,
        verbose_name='Дата рождения',
        help_text="Нельзя оставить пустым"
    )

    def __str__(self):
        return f"{self.name_rus} {self.surname_rus}"

    class Meta:
        verbose_name = 'Актеры'

    def save(self, *args, **kwargs):
        if self.image:
            img = Image.open(self.image)
            buffer = BytesIO()
            img_format = img.format.lower()
            img.save(buffer, format=img_format)
            image_base64_str = base64.b64encode(buffer.getvalue()).decode('utf-8')
            self.image_base64 = f"data:image/{img_format};base64,{image_base64_str}"
        super().save(*args, **kwargs)

class Film(models.Model):
    image = models.ImageField(
        null=False,
        blank=False,
        upload_to="static/images/",
        verbose_name='Фотография фильма',
        help_text="Ставьте небольшого объема картинки. Нельзя оставить пустым!",
    )
    image_base64 = models.TextField(
        blank=True,
        null=True,
        verbose_name='Не трогать это поле!',
        help_text="Не трогать это поле!"
    )
    name_rus = models.CharField(
        max_length=250,
        null=False,
        blank=False,
        unique=False,
        verbose_name="Название фильма на русском",
        help_text="Нельзя оставить пустым"
    )
    name_eng = models.CharField(
        max_length=250,
        null=False,
        blank=False,
        unique=False,
        verbose_name="Название фильма на английском",
        help_text="Нельзя оставить пустым"
    )
    name_tkm = models.CharField(
        max_length=250,
        null=False,
        blank=False,
        unique=False,
        verbose_name="Название фильма на туркменском",
        help_text="Нельзя оставить пустым",
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
    actors = models.ManyToManyField(Actors, related_name='Films')

    def __str__(self):
        return self.name_rus

    def save(self, *args, **kwargs):
        if self.image:
            img = Image.open(self.image)
            buffer = BytesIO()
            img_format = img.format.lower()
            img.save(buffer, format=img_format)
            image_base64_str = base64.b64encode(buffer.getvalue()).decode('utf-8')
            self.image_base64 = f"data:image/{img_format};base64,{image_base64_str}"
        super().save(*args, **kwargs)