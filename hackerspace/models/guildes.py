from django.db import models

from hackerspace.models import Event
from hackerspace.models.events import updateTime


class Guilde(models.Model):
    str_name = models.CharField(max_length=250, blank=True, null=True)
    url_featured_photo = models.URLField(max_length=200, blank=True, null=True)
    text_description = models.TextField(blank=True, null=True)
    many_members = models.ManyToManyField(
        'Person', related_name="m_members", blank=True)
    int_UNIXtime_created = models.IntegerField(blank=True, null=True)
    int_UNIXtime_updated = models.IntegerField(blank=True, null=True)

    def __str__(self):
        return self.str_name

    @property
    def events(self):
        return Event.objects.by_guilde(one_guilde=self)

    def save(self, *args, **kwargs):
        self = updateTime(self)
        super(Guilde, self).save(*args, **kwargs)
