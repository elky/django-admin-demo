# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models
from django.utils import timezone


class NewsEntry(models.Model):
    STATUS_CHOICES = [
        (0, 'Draft'),
        (1, 'Published'),
        (2, 'Moderation'),
    ]

    title = models.CharField(max_length=300)
    slug = models.SlugField()
    summary = models.TextField()
    featured_image = models.ImageField(upload_to='uploads/news', blank=True,
                                       help_text='Recommended image resolution: 720x400 pixels')
    status = models.PositiveSmallIntegerField(choices=STATUS_CHOICES, default=0)
    source = models.URLField(blank=True, help_text='Link to a source. Will be shown at the bottom of the news page')
    author = models.ForeignKey('authors.Author', help_text='Current user if empty')
    tags = models.ManyToManyField('tags.Tag', blank=True)
    created_at = models.DateTimeField(default=timezone.now)
    modified_at = models.DateTimeField(default=timezone.now)

    class Meta:
        verbose_name = 'Entry'
        verbose_name_plural = 'Entries'

    def __unicode__(self):
        return self.title

    def get_absolute_url(self):
        return 'http://demo.elky.me/'


class NewsGallery(models.Model):
    entry = models.ForeignKey('news.NewsEntry')
    image = models.ImageField(upload_to='uploads/news')
    description = models.CharField(max_length=200, blank=True)
    copyright = models.CharField(max_length=200, blank=True)

    class Meta:
        verbose_name = 'Gallery item'
        verbose_name_plural = 'News gallery'

    def __unicode__(self):
        return 'Image #%d' % self.id
