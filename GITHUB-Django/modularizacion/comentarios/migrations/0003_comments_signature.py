# Generated by Django 4.0.5 on 2022-06-19 05:31

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('comentarios', '0002_comments_date'),
    ]

    operations = [
        migrations.AddField(
            model_name='comments',
            name='signature',
            field=models.CharField(default='firma', max_length=100),
        ),
    ]
