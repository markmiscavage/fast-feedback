from django.db import models


class Feedback(models.Model):
    text = models.TextField(blank=True)
    email = models.TextField(blank=True)


    def __unicode__(self):
        return self.text
