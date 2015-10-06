from django.db import models


class Photo(models.Model):
    photo_id = models.AutoField(primary_key=True)
    title = models.CharField(max_length=255)
    description = models.TextField(blank=True)
    path = models.ImageField(upload_to='photos')
    isActive = models.BooleanField(default=True)
    last_update = models.DateTimeField(auto_now=True)

    class Meta:
        ordering = ["photo_id"]

    def __unicode__(self):
        return u'%s' % self.title