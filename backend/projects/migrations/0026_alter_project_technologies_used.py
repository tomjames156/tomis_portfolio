# Generated by Django 4.2.6 on 2023-10-26 10:18

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('projects', '0025_alter_project_project_image_alter_screenshot_project'),
    ]

    operations = [
        migrations.AlterField(
            model_name='project',
            name='technologies_used',
            field=models.ManyToManyField(null=True, related_name='projects', to='projects.technologyused'),
        ),
    ]
