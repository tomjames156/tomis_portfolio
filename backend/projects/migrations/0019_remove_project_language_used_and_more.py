# Generated by Django 4.2.6 on 2023-10-25 22:27

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('projects', '0018_project_project_image'),
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
            name='languages_used',
            field=models.ManyToManyField(related_name='stack', to='projects.languageused'),
        ),
        migrations.AddField(
            model_name='project',
            name='technologies_used',
            field=models.ManyToManyField(related_name='projects', to='projects.technologyused'),
        ),
    ]