from django.db import models


class Menu(models.Model):
    menu_id = models.AutoField(primary_key=True)
    title = models.CharField(max_length=255, blank=False)
    type = models.CharField(max_length=20,
                            help_text="1-starter, 2-entree, 3-dessert")
    description = models.TextField(blank=True)
    recipe = models.TextField(blank=True)
    photo = models.ImageField(upload_to='menu', blank=True)
    isActive = models.BooleanField(default=True)
    last_update = models.DateTimeField(auto_now=True)

    class Meta:
        ordering = ["menu_id"]

    def __unicode__(self):
        return u'%s' % self.title
