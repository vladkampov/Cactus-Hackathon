from django.db import models
from personal.models import Profile

REQUEST_INTERVAL = 60


class Stream(models.Model):
    thumbnail = models.ImageField('stream_thumbnail', upload_to='thumbnail',
                                  height_field='preview_width',
                                  width_field='preview_height')
    preview_width = models.IntegerField(default=120)
    preview_height = models.IntegerField(default=200)
    owner = models.ForeignKey(Profile)
    url = models.URLField()
    views = models.IntegerField()
    title = models.CharField(max_length=50)
    description = models.CharField(max_length=150)
    is_active = models.BooleanField()

    def __str__(self):
        return "%s - %s" % (self.title, self.url)


class Statistics(models.Model):
    stream = models.ForeignKey(Stream)
    user = models.ForeignKey(Profile)
    spent_time = models.IntegerField()
