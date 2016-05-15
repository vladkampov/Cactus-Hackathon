from django.db import models
from personal.models import Profile


class Stream(models.Model):
    thumbnail = models.ImageField('stream_thumbnail', upload_to='thumbnail',
                                  height_field='preview_width',
                                  width_field='preview_height')
    preview_width = models.IntegerField(default=120)
    preview_height = models.IntegerField(default=200)
    url = models.URLField()
    views = models.IntegerField()
    title = models.CharField(max_length=50)
    description = models.CharField(max_length=150)
    is_active = models.BooleanField()
    owner = models.ForeignKey(Profile)

    def __str__(self):
        return "%s - %s" % (self.title, self.url)
