# Generated by Django 3.0.6 on 2020-07-25 02:58

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('recipes', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='recipe',
            name='cuisine',
            field=models.CharField(default='American', max_length=75),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='recipe',
            name='difficulty',
            field=models.CharField(default='Medium', max_length=75),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='recipe',
            name='mealType',
            field=models.CharField(default='Any', max_length=75),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='recipe',
            name='nutrition',
            field=models.CharField(default='Well-Rounded', max_length=75),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='recipe',
            name='recipeLink',
            field=models.CharField(default='No Link', max_length=200),
            preserve_default=False,
        ),
    ]
