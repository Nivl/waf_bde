# -*- coding: utf-8 -*-

from django.db import models


class Product(models.Model):
    name = models.CharField(
        max_length=255,
        verbose_name=u'nom')

    image = models.ImageField(
        upload_to='market/products/',
        verbose_name=u'image',
        help_text='Résolution : 350x200')

    description = models.TextField(
        verbose_name=u'description')

    price = models.PositiveIntegerField(
        verbose_name=u'prix')

    quantity = models.PositiveIntegerField(
        default=0,
        verbose_name=u'quantité',
        help_text=u'0 = infinie'
        )

    def __unicode__(self):
        return self.name

    class Meta:
        verbose_name = u'Produit'
        verbose_name_plural = u'Produits'
