from django.db import models


class Poll(models.Model):
    pub_date = models.DateField(
        auto_now_add=True,
        verbose_name=u'date de publication')

    name = models.CharField(
        max_length=255,
        verbose_name=u'nom')

    def __unicode__(self):
        return self.name

    class Meta:
        ordering = ['-pub_date']
        verbose_name = u'Sondage'
        verbose_name_plural = u'Sondages'


class Choice(models.Model):
    poll = models.ForeignKey(
        Poll,
        verbose_name=u'sondage')

    name = models.CharField(
        max_length=255,
        verbose_name=u'nom')

    order = models.PositiveSmallIntegerField(
        default=0,
        verbose_name=u'ordre')

    votes = models.PositiveIntegerField(
        default=0,
        verbose_name=u'votes')

    def __unicode__(self):
        return self.poll.__unicode__()

    class Meta:
        ordering = ['order']
        verbose_name = u'Choix'
        verbose_name_plural = u'Choix'
