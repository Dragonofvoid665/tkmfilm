# Generated by Django 5.1.4 on 2025-05-22 15:00

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('films', '0004_remove_studiohistorysssr_creator_bio_eng_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='film',
            name='sssr_or_not',
            field=models.BooleanField(default=False, help_text='Нельзя оставлять пустым', verbose_name='Снят при СССР или нет'),
        ),
    ]
