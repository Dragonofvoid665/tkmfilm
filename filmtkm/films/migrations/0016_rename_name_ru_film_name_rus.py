# Generated by Django 5.1.4 on 2025-05-30 07:22

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('films', '0015_remove_actors_kadr1_remove_actors_kadr2_and_more'),
    ]

    operations = [
        migrations.RenameField(
            model_name='film',
            old_name='name_ru',
            new_name='name_rus',
        ),
    ]
