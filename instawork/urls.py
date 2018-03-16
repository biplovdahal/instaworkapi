from django.conf.urls import *
from instaworkapi.views import listings


urlpatterns = patterns('',
    # this URL passes resource_id in **kw to MyRESTView
    url(r'^', listings.as_view(), name='my_rest_view'),
)
