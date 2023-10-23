# Generated by Django 4.2.6 on 2023-10-23 21:49

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('projects', '0009_alter_project_importance'),
    ]

    operations = [
        migrations.AlterField(
            model_name='project',
            name='importance',
            field=models.CharField(choices=[('1', 'complex'), ('2', 'proud of'), ('3', 'easy')], default='1', max_length=1),
        ),
    ]
