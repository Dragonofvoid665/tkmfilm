# Generated by Django 5.1.4 on 2025-05-19 15:33

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Actors',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('image', models.ImageField(help_text='Ставьте небольшие по объёму картинки. Нельзя оставить пустым!', upload_to='static/images/', verbose_name='Фотография')),
                ('name_rus', models.CharField(help_text='Нельзя оставить пустым', max_length=100, verbose_name='Имя на русском')),
                ('name_eng', models.CharField(help_text='Нельзя оставить пустым', max_length=100, verbose_name='Имя на английском')),
                ('name_tkm', models.CharField(help_text='Нельзя оставить пустым', max_length=100, verbose_name='Имя на туркменском')),
                ('surname_rus', models.CharField(help_text='Нельзя оставить пустым', max_length=100, verbose_name='Фамилия на русском')),
                ('surname_eng', models.CharField(help_text='Нельзя оставить пустым', max_length=100, verbose_name='Фамилия на английском')),
                ('surname_tkm', models.CharField(help_text='Нельзя оставить пустым', max_length=100, verbose_name='Фамилия на туркменском')),
                ('father_name_rus', models.CharField(help_text='Нельзя оставить пустым', max_length=50, verbose_name='Отчество на русском')),
                ('father_name_eng', models.CharField(help_text='Нельзя оставить пустым', max_length=50, verbose_name='Отчество на английском')),
                ('father_name_tkm', models.CharField(help_text='Нельзя оставить пустым', max_length=50, verbose_name='Отчество на туркменском')),
                ('biography_rus', models.TextField(help_text='Нельзя оставить пустым', verbose_name='Биография на русском')),
                ('biography_eng', models.TextField(help_text='Нельзя оставить пустым', verbose_name='Биография на английском')),
                ('biography_tkm', models.TextField(help_text='Нельзя оставить пустым', verbose_name='Биография на туркменском')),
                ('birth_date', models.DateField(help_text='Нельзя оставить пустым', verbose_name='Дата рождения')),
                ('sssr_or_not', models.BooleanField(default=False)),
            ],
            options={
                'verbose_name': 'Актёр',
                'verbose_name_plural': 'Актёры',
            },
        ),
        migrations.CreateModel(
            name='Director',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('image', models.ImageField(help_text='Ставьте небольшие по объёму картинки. Нельзя оставить пустым!', upload_to='static/images/', verbose_name='Фотография')),
                ('name_rus', models.CharField(help_text='Нельзя оставить пустым', max_length=100, verbose_name='Имя на русском')),
                ('name_eng', models.CharField(help_text='Нельзя оставить пустым', max_length=100, verbose_name='Имя на английском')),
                ('name_tkm', models.CharField(help_text='Нельзя оставить пустым', max_length=100, verbose_name='Имя на туркменском')),
                ('surname_rus', models.CharField(help_text='Нельзя оставить пустым', max_length=100, verbose_name='Фамилия на русском')),
                ('surname_eng', models.CharField(help_text='Нельзя оставить пустым', max_length=100, verbose_name='Фамилия на английском')),
                ('surname_tkm', models.CharField(help_text='Нельзя оставить пустым', max_length=100, verbose_name='Фамилия на туркменском')),
                ('father_name_rus', models.CharField(help_text='Нельзя оставить пустым', max_length=50, verbose_name='Отчество на русском')),
                ('father_name_eng', models.CharField(help_text='Нельзя оставить пустым', max_length=50, verbose_name='Отчество на английском')),
                ('father_name_tkm', models.CharField(help_text='Нельзя оставить пустым', max_length=50, verbose_name='Отчество на туркменском')),
                ('biography_rus', models.TextField(help_text='Нельзя оставить пустым', verbose_name='Биография на русском')),
                ('biography_eng', models.TextField(help_text='Нельзя оставить пустым', verbose_name='Биография на английском')),
                ('biography_tkm', models.TextField(help_text='Нельзя оставить пустым', verbose_name='Биография на туркменском')),
                ('birth_date', models.DateField(help_text='Нельзя оставить пустым', verbose_name='Дата рождения')),
                ('sssr_or_not', models.BooleanField(default=False)),
            ],
            options={
                'verbose_name': 'Режиссёр',
                'verbose_name_plural': 'Режиссёры',
            },
        ),
        migrations.CreateModel(
            name='News',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('image', models.ImageField(help_text='Ставьте небольшие по объёму картинки. Нельзя оставить пустым!', upload_to='static/images/', verbose_name='Фотография')),
                ('title_rus', models.CharField(help_text='Нельзя оставить пустым', max_length=200, verbose_name='Заголовок новости на русском')),
                ('title_eng', models.CharField(help_text='Нельзя оставить пустым', max_length=200, verbose_name='Заголовок новости на английском')),
                ('title_tkm', models.CharField(help_text='Нельзя оставить пустым', max_length=200, verbose_name='Заголовок новости на туркменском')),
                ('content_rus', models.TextField(help_text='Нельзя оставить пустым', verbose_name='Текст новости на русском')),
                ('content_eng', models.TextField(help_text='Нельзя оставить пустым', verbose_name='Текст новости на английском')),
                ('content_tkm', models.TextField(help_text='Нельзя оставить пустым', verbose_name='Текст новости на туркменском')),
                ('publication_date', models.DateField(help_text='Нельзя оставить пустым', verbose_name='Дата публикации')),
            ],
            options={
                'verbose_name': 'Новость',
                'verbose_name_plural': 'Новости',
            },
        ),
        migrations.CreateModel(
            name='Screenwriter',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('image', models.ImageField(help_text='Ставьте небольшие по объёму картинки. Нельзя оставить пустым!', upload_to='static/images/', verbose_name='Фотография')),
                ('name_rus', models.CharField(help_text='Нельзя оставить пустым', max_length=100, verbose_name='Имя на русском')),
                ('name_eng', models.CharField(help_text='Нельзя оставить пустым', max_length=100, verbose_name='Имя на английском')),
                ('name_tkm', models.CharField(help_text='Нельзя оставить пустым', max_length=100, verbose_name='Имя на туркменском')),
                ('surname_rus', models.CharField(help_text='Нельзя оставить пустым', max_length=100, verbose_name='Фамилия на русском')),
                ('surname_eng', models.CharField(help_text='Нельзя оставить пустым', max_length=100, verbose_name='Фамилия на английском')),
                ('surname_tkm', models.CharField(help_text='Нельзя оставить пустым', max_length=100, verbose_name='Фамилия на туркменском')),
                ('father_name_rus', models.CharField(help_text='Нельзя оставить пустым', max_length=50, verbose_name='Отчество на русском')),
                ('father_name_eng', models.CharField(help_text='Нельзя оставить пустым', max_length=50, verbose_name='Отчество на английском')),
                ('father_name_tkm', models.CharField(help_text='Нельзя оставить пустым', max_length=50, verbose_name='Отчество на туркменском')),
                ('biography_rus', models.TextField(help_text='Нельзя оставить пустым', verbose_name='Биография на русском')),
                ('biography_eng', models.TextField(help_text='Нельзя оставить пустым', verbose_name='Биография на английском')),
                ('biography_tkm', models.TextField(help_text='Нельзя оставить пустым', verbose_name='Биография на туркменском')),
                ('birth_date', models.DateField(help_text='Нельзя оставить пустым', verbose_name='Дата рождения')),
                ('sssr_or_not', models.BooleanField(default=False)),
            ],
            options={
                'verbose_name': 'Сценарист',
                'verbose_name_plural': 'Сценаристы',
            },
        ),
        migrations.CreateModel(
            name='StudioHistory',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('image', models.ImageField(help_text='Ставьте небольшие по объёму картинки. Нельзя оставить пустым!', upload_to='static/images/', verbose_name='Фотография')),
                ('text_rus', models.TextField(help_text='Нельзя оставить пустым', verbose_name='Информация о студии на русском')),
                ('text_eng', models.TextField(help_text='Нельзя оставить пустым', verbose_name='Информация о студии на английском')),
                ('text_tkm', models.TextField(help_text='Нельзя оставить пустым', verbose_name='Информация о студии на туркменском')),
                ('creator_bio_rus', models.TextField(help_text='Нельзя оставить пустым', verbose_name='Биография создателя студии на русском')),
                ('creator_bio_eng', models.TextField(help_text='Нельзя оставить пустым', verbose_name='Биография создателя студии на английском')),
                ('creator_bio_tkm', models.TextField(help_text='Нельзя оставить пустым', verbose_name='Биография создателя студии на туркменском')),
                ('found_date', models.DateField(help_text='Нельзя оставить пустым', verbose_name='Дата основания студии')),
                ('creator_birth_date', models.DateField(help_text='Нельзя оставить пустым', verbose_name='Дата рождения создателя')),
            ],
            options={
                'verbose_name': 'История студии',
                'verbose_name_plural': 'История студии',
            },
        ),
        migrations.CreateModel(
            name='Film',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('image', models.ImageField(help_text='Ставьте небольшие по объёму картинки. Нельзя оставить пустым!', upload_to='static/images/', verbose_name='Фотография')),
                ('name_rus', models.CharField(help_text='Нельзя оставить пустым', max_length=200, verbose_name='Название фильма на русском')),
                ('name_eng', models.CharField(help_text='Нельзя оставить пустым', max_length=200, verbose_name='Название фильма на английском')),
                ('name_tkm', models.CharField(help_text='Нельзя оставить пустым', max_length=200, verbose_name='Название фильма на туркменском')),
                ('description_rus', models.TextField(help_text='Нельзя оставить пустым', verbose_name='Описание фильма на русском')),
                ('description_eng', models.TextField(help_text='Нельзя оставить пустым', verbose_name='Описание фильма на английском')),
                ('description_tkm', models.TextField(help_text='Нельзя оставить пустым', verbose_name='Описание фильма на туркменском')),
                ('genre_eng', models.CharField(help_text='Нельзя оставить пустым', max_length=100, verbose_name='Жанр фильма на анлийском')),
                ('genre_rus', models.CharField(help_text='Нельзя оставить пустым', max_length=100, verbose_name='Жанр фильма на русском')),
                ('genre_tkm', models.CharField(help_text='Нельзя оставить пустым', max_length=100, verbose_name='Жанр фильма на туркменском')),
                ('some_field', models.CharField(blank=True, max_length=200, null=True)),
                ('actors', models.ManyToManyField(related_name='films', to='films.actors')),
                ('director', models.ManyToManyField(related_name='films', to='films.director')),
                ('screenwriters', models.ManyToManyField(related_name='films', to='films.screenwriter')),
            ],
            options={
                'verbose_name': 'Фильм',
                'verbose_name_plural': 'Фильмы',
            },
        ),
    ]
