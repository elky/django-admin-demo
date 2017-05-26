# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models


class Author(models.Model):
    name = models.CharField(max_length=300)
    avatar = models.ImageField(upload_to='uploads/avatars')
    bio = models.TextField(blank=True)
    position = models.ForeignKey('authors.Position')
    active = models.BooleanField(default=True)

    def __unicode__(self):
        return self.name


class Position(models.Model):
    title = models.CharField(max_length=200)

    def __unicode__(self):
        return self.title


class SocialLink(models.Model):
    SOCIAL_CHOICES = [
        ('website', 'Website'),
        ('twitter', 'Twitter'),
        ('facebook', 'Facebook'),
        ('instagram', 'Instagram'),
    ]

    author = models.ForeignKey('authors.Author')
    social = models.CharField(max_length=20, choices=SOCIAL_CHOICES)
    link = models.URLField()

    def __unicode__(self):
        return self.social
