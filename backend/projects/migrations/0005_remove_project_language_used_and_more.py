# Generated by Django 4.2.6 on 2023-10-23 21:30

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('projects', '0004_project_language_used_project_technology_used_and_more'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='project',
            name='language_used',
        ),
        migrations.RemoveField(
            model_name='project',
            name='technology_used',
        ),
        migrations.AddField(
            model_name='project',
            name='language_used',
            field=models.ManyToManyField(to='projects.languageused'),
        ),
        migrations.AddField(
            model_name='project',
            name='technology_used',
            field=models.ManyToManyField(to='projects.technologyused'),
        ),
    ]