# Generated by Django 3.0.3 on 2020-06-26 06:10

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('AppProyecto', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='cuestionario',
            name='pregunta9',
            field=models.CharField(blank=True, max_length=200, null=True),
        ),
    ]
