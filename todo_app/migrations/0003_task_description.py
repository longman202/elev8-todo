# Generated by Django 4.0.4 on 2022-05-11 16:03

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('todo_app', '0002_task_category'),
    ]

    operations = [
        migrations.AddField(
            model_name='task',
            name='description',
            field=models.CharField(blank=True, max_length=400, null=True, verbose_name='Describe your task'),
        ),
    ]