# Generated by Django 3.0.8 on 2022-12-15 23:56

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0004_task_finished'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='task',
            name='important',
        ),
    ]
