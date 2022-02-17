# Generated by Django 4.0.1 on 2022-01-19 12:53

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Album',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=20)),
                ('date', models.DateField()),
                ('cover', models.URLField(blank=True)),
            ],
        ),
        migrations.CreateModel(
            name='Artis',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=30)),
                ('yonalish', models.CharField(blank=True, max_length=20)),
                ('description', models.TextField()),
                ('image', models.URLField(blank=True)),
            ],
        ),
        migrations.CreateModel(
            name='Song',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=20)),
                ('cover', models.URLField(blank=True)),
                ('lyrics', models.TextField(blank=True)),
                ('duration', models.DurationField()),
                ('sourse', models.URLField(blank=True)),
                ('albom', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='musicapp.album')),
            ],
        ),
        migrations.AddField(
            model_name='album',
            name='artist',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='musicapp.artis'),
        ),
    ]
