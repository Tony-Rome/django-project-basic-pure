# Generated by Django 2.2 on 2020-11-04 01:14

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0007_auto_20201104_0113'),
    ]

    operations = [
        migrations.AlterField(
            model_name='writer',
            name='timestamp',
            field=models.DateTimeField(auto_now_add=True),
        ),
    ]