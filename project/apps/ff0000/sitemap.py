from django.contrib.sitemaps import Sitemap
from django.core.urlresolvers import reverse
import datetime

# Go here. Read: https://docs.djangoproject.com/en/1.7/ref/contrib/sitemaps/

class BaseSitemap(Sitemap):
    def __init__(self, names):
        """
        :param names:
        :return:

        Takes the reverse names from urlpatterns.
        """
        self.names = names

    def items(self):
        return self.names

    def changefreq(self, obj):
        return 'daily'

    def lastmod(self, obj):
        return datetime.datetime.now()

    def location(self, obj):
        return reverse(obj)
