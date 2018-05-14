from django.db import models

from scarlet.assets.fields import AssetsFileField
from scarlet.assets.models import Asset


# Looking to supress create_superuser prompt? Use below insted.
#
# python manage.py migrate --noinput
#


class SEO(models.Model):
    title = models.CharField(
        blank=True, max_length=200, help_text='Not used, only for bookkeeping')

    meta_title = models.CharField(blank=True, max_length=200)
    meta_description = models.CharField(blank=True, max_length=200)
    meta_keywords = models.CharField(blank=True, max_length=200)


class SocialGraph(models.Model):
    og_site_name = models.CharField(blank=True, max_length=200)
    og_title = models.CharField(blank=True, max_length=200)
    og_description = models.CharField(blank=True, max_length=200)
    og_image = AssetsFileField(
        blank=True, null=True, type=Asset.IMAGE, tags=['meta'])

    class Meta:
        abstract = True

    def __unicode__(self):
        return self.title or self.meta_title
