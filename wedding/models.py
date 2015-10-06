from django.db import models


class Comment(models.Model):
    comment_id = models.AutoField(primary_key=True)
    person_name = models.CharField(max_length=255, blank=False,
                                   default="Anonymous")
    comment = models.TextField(blank=True)
    isActive = models.BooleanField(default=True)
    last_update = models.DateTimeField(auto_now=True)

    class Meta:
        ordering = ["last_update"]

    def __unicode__(self):
        return u'%s' % self.person_name
