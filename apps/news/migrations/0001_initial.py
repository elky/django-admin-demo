# -*- coding: utf-8 -*-
# Generated by Django 1.11.1 on 2017-05-26 23:12
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion
import django.utils.timezone


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('authors', '0001_initial'),
        ('tags', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='NewsEntry',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=300)),
                ('slug', models.SlugField()),
                ('summary', models.TextField()),
                ('featured_image', models.ImageField(blank=True, help_text='Recommended image resolution: 720x400 pixels', upload_to='uploads/news')),
                ('status', models.PositiveSmallIntegerField(choices=[(0, 'Draft'), (1, 'Published'), (2, 'Moderation')], default=0)),
                ('source', models.URLField(blank=True, help_text='Link to a source. Will be shown at the bottom of the news page')),
                ('created_at', models.DateTimeField(default=django.utils.timezone.now)),
                ('modified_at', models.DateTimeField(default=django.utils.timezone.now)),
                ('author', models.ForeignKey(help_text='Current user if empty', on_delete=django.db.models.deletion.CASCADE, to='authors.Author')),
                ('tags', models.ManyToManyField(blank=True, to='tags.Tag')),
            ],
            options={
                'verbose_name_plural': 'News entries',
            },
        ),
        migrations.CreateModel(
            name='NewsGallery',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('image', models.ImageField(upload_to='uploads/news')),
                ('description', models.CharField(blank=True, max_length=200)),
                ('copyright', models.CharField(blank=True, max_length=200)),
                ('entry', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='news.NewsEntry')),
            ],
            options={
                'verbose_name': 'Gallery item',
                'verbose_name_plural': 'News gallery',
            },
        ),
    ]
