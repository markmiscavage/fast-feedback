
from django.conf import settings
from django.conf.urls import include, url
from django.conf.urls.static import static
from django.contrib.sitemaps.views import sitemap
from django.views.generic import TemplateView

from scarlet.cms.sites import site

from apps.ff0000.sitemap import BaseSitemap
from apps.feedback import views

sitemaps = {'pages': BaseSitemap(['homepage']), }

urlpatterns = [
    url(r'^admin/', include(site.urls)),
    url(r'^feedback/$', views.FeedbackView),
]

# Static files and debug error pages only get served by django in DEBUG mode
if settings.DEBUG:
    # 404 and 500 error page debugging
    urlpatterns += [
        url(r'^500$', TemplateView.as_view(template_name='500.html')),
        url(r'^404$', TemplateView.as_view(template_name='404.html')),
    ]
    urlpatterns += static(settings.MEDIA_URL,
                          document_root=settings.MEDIA_ROOT)