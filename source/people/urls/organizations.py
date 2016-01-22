from django.conf import settings
from django.conf.urls.defaults import *
from django.views.decorators.cache import cache_page

from source.people.views import OrganizationList, OrganizationDetail, OrganizationUpdate

STANDARD_CACHE_TIME = getattr(settings, 'CACHE_MIDDLEWARE_SECONDS', 60*15)

urlpatterns = patterns('',
    url(
        regex = '^$',
        view = cache_page(OrganizationList.as_view(), STANDARD_CACHE_TIME),
        kwargs = {},
        name = 'organization_list',
    ),
    url(
        regex = '^update/$',
        view = OrganizationUpdate.as_view(),
        kwargs = {},
        name = 'organization_update',
    ),
    url(
        regex = '^(?P<slug>[-\w]+)/$',
        view = cache_page(OrganizationDetail.as_view(), STANDARD_CACHE_TIME),
        kwargs = {},
        name = 'organization_detail',
    ),
)
