# Generated by Django 3.0.8 on 2022-12-15 22:57

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='task',
            old_name='contenido',
            new_name='content',
        ),
        migrations.RenameField(
            model_name='task',
            old_name='titulo',
            new_name='title',
        ),
        migrations.AddField(
            model_name='task',
            name='finished',
            field=models.BooleanField(null=True),
        ),
    ]
