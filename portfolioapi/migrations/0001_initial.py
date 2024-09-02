# Generated by Django 5.1 on 2024-09-02 06:36

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='GitHubStats',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('repos', models.IntegerField(blank=True, default=30, null=True)),
                ('YTDcontributions', models.IntegerField(blank=True, default=431, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='LanguageTag',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=20, unique=True)),
            ],
        ),
        migrations.CreateModel(
            name='Project',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=20)),
                ('description', models.TextField(max_length=2000)),
                ('deployed', models.BooleanField(default=False)),
                ('tags', models.ManyToManyField(related_name='projects', to='portfolioapi.languagetag')),
            ],
        ),
        migrations.CreateModel(
            name='Image',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('image', models.ImageField(blank=True, null=True, upload_to='projectImages/')),
                ('caption', models.CharField(blank=True, max_length=255, null=True)),
                ('project', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='images', to='portfolioapi.project')),
            ],
        ),
    ]
