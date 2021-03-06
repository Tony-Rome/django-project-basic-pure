# Generated by Django 2.2 on 2020-11-07 21:23

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('stories', '0001_initial'),
        ('stories_routes', '0001_initial'),
        ('writers', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='comment',
            name='story',
            field=models.OneToOneField(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='stories.Story'),
        ),
        migrations.AddField(
            model_name='comment',
            name='story_route',
            field=models.OneToOneField(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='stories_routes.StoryRoute'),
        ),
    ]
