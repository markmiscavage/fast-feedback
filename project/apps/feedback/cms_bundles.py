from scarlet.cms import bundles, views
from scarlet.cms.sites import site

from . import models


class FeedbackBundle(bundles.Bundle):
    dashboard = (('email', 'text'), )

    main = views.ListView(paginate_by=20)

    class Meta:
        model = models.Feedback

site.register("feedback", FeedbackBundle(name='feedback', title='Feedback'), order=1)
