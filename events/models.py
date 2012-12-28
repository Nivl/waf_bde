# -*- coding: utf-8 -*-

from django.db import models


class Event(models.Model):
    name = models.CharField(
        max_length=255,
        verbose_name=u'nom')

    poster = models.ImageField(
        upload_to='events/posters/',
        blank=True,
        null=True,
        verbose_name=u'affiche')

    start_date = models.DateTimeField(
        verbose_name=u'date de debut')

    end_date = models.DateTimeField(
        verbose_name=u'date de fin')

    price = models.PositiveIntegerField(
        default=0,
        verbose_name=u'prix')

    nb_places = models.PositiveIntegerField(
        default=0,
        verbose_name=u'Nombre de places',
        help_text=u'0 = illimité')

    description = models.TextField(
        verbose_name=u'description',
        help_text=u'Markdown activé')

    class Meta:
        ordering = ['-start_date']
        verbose_name = u'Évènement'
        verbose_name_plural = u'Évènements'
